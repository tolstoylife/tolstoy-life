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
    parts = re.split(r'(?<=[.!?"])\s+(?=["“(A-ZА-Я])', text)
    return [p.replace("<DOT>", ".").strip() for p in parts if p.strip()]
