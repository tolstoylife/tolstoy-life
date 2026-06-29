"""Display text -> speech text. Ported from projects/audiobook/flow_preprocess.py
(phrasing fixes) and build_audiobook.py SUBS (pronunciation respellings), so the
segmenter owns these rules and segments.json carries final speech text.
The display text stays faithful; we only reshape what the TTS hears."""
import re

_CONJ = r"(?:and|but|or|nor|yet|so|for)\b"

# Pronunciation respellings for Kokoro's g2p (verbatim from build_audiobook.py SUBS).
_SUBS = [
    (r"\blive\b", "liv"),
    (r"\bLabouchere\b", "Labooshair"),
    (r"\bRadischeff\b", "Rahdeeshef"),
    (r"Yasnaya Poliana", "Yasnaya Polyahna"),
    (r"\(Matt[.,] xxiii\. 27, 28\)",
     "Matthew twenty-three, verses twenty-seven and twenty-eight"),
]

def _fix_ellipsis(t):
    t = t.replace("...", "…")
    return re.sub(r"\.\s*\.\s*\.", "…", t)

def _fix_semicolons(t):
    t = re.sub(rf";\s+({_CONJ})", r", \1", t)            # "; and" -> ", and"
    return re.sub(r";\s+([a-zA-Z])", lambda m: ". " + m.group(1).upper(), t)

def _fix_dashes(t):
    t = t.replace("—", " — ")
    return re.sub(r"\s{2,}", " ", t)

def _respell(t):
    for pat, rep in _SUBS:
        t = re.sub(pat, rep, t)
    return t

def to_speech(text):
    text = re.sub(r"\[\^\w+\]", "", text)                # drop footnote markers (skippable in audio)
    text = _fix_ellipsis(text)
    text = _fix_semicolons(text)
    text = _fix_dashes(text)
    text = _respell(text)
    return text.strip()
