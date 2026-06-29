"""Markdown (one version of a work) -> segments.json (the shared contract).
Each sentence gets a stable two-layer ID, its faithful display text, and its
speech text. The spine (Russian) defines the paragraph coordinate; translations
are validated as paragraph-parallel."""
import re, json, sys, argparse
from pathlib import Path
from reader import ids
from reader.speech import to_speech

# ── CriticMarkup → reading text ────────────────────────────────────────────────
def resolve_reading_text(md):
    md = re.sub(r"\{>>.*?<<\}", "", md, flags=re.S)         # notes: drop
    md = re.sub(r"\{--(.*?)--\}", "", md, flags=re.S)       # deletions: drop
    md = re.sub(r"\{\+\+(.*?)\+\+\}", r"\1", md, flags=re.S)# insertions: keep
    md = re.sub(r"\{~~(.*?)~>(.*?)~~\}", r"\2", md, flags=re.S)  # change: keep new
    md = re.sub(r"\{==(.*?)==\}", r"\1", md, flags=re.S)    # highlight: keep
    md = re.sub(r"\[\[([^\]]+)\]\]", r"\1", md)             # wikilink: keep label
    return re.sub(r"[ \t]{2,}", " ", md).strip()

# ── Sentence split (ported from build_audiobook.split_sents) ───────────────────
def split_sentences(text):
    text = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", text)        # protect 1.40
    # Split on whitespace after terminal punctuation. A footnote marker may sit
    # between the punctuation and the space ("cow.[^1] I") — keep it glued to the
    # sentence it ends, then split on a sentinel so the boundary still fires.
    text = re.sub(r'(?<=[.!?"])(\[\^\w+\])?\s+(?=["“(A-ZА-Я])', r"\1<SPLIT>", text)
    parts = text.split("<SPLIT>")
    return [p.replace("<DOT>", ".").strip() for p in parts if p.strip()]

# ── Heading spoken form (ported from build_audiobook.spoken_header) ────────────
_ROMAN = {"I":"One","II":"Two","III":"Three","IV":"Four","V":"Five",
          "VI":"Six","VII":"Seven","VIII":"Eight","IX":"Nine"}

def heading_speech(heading):
    m = re.match(r"Part ([IVX]+)\s*$", heading.strip())
    if m and m.group(1) in _ROMAN:
        return f"Part {_ROMAN[m.group(1)]}."
    return heading.strip().rstrip(".") + "."

# ── Structure parse ────────────────────────────────────────────────────────────
def _note_defs(md):
    """Pull '[^label]: text' definitions out; return (body_without_defs, notes)."""
    notes, n = [], 0
    def repl(m):
        nonlocal n
        n += 1
        notes.append({"id": ids.note_id(n), "label": m.group(1),
                      "html": m.group(2).strip()})
        return ""
    body = re.sub(r"^\[\^(\w+)\]:[ \t]*(.+)$", repl, md, flags=re.M)
    return body, notes

def parse(md):
    body, notes = _note_defs(md)
    # split into sections on '## ' headings; text before the first heading is ignored here
    chunks = re.split(r"^##\s+(.+)$", body, flags=re.M)
    sections = []
    # chunks = [pre, heading1, body1, heading2, body2, ...]
    sec_n = 0
    for i in range(1, len(chunks), 2):
        sec_n += 1
        heading = chunks[i].strip()
        sec = {"id": ids.section_id(sec_n), "heading": heading,
               "headingSpeech": heading_speech(heading), "paragraphs": []}
        paras = [p.strip() for p in re.split(r"\n\s*\n", chunks[i + 1]) if p.strip()]
        for pn, raw in enumerate(paras, start=1):
            pid = ids.paragraph_id(sec_n, pn)
            reading = resolve_reading_text(raw)
            sentences = []
            for sk, sent in enumerate(split_sentences(reading), start=1):
                sentences.append({"id": ids.sentence_id(pid, sk),
                                  "display": sent, "speech": to_speech(sent)})
            sec["paragraphs"].append({"id": pid, "sentences": sentences})
        sections.append(sec)
    return {"sections": sections, "notes": notes}
