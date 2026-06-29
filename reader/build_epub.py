# reader/build_epub.py
"""Package a version's XHTML + timing.json into a read-along EPUB3.
ebooklib only zips the container; the SMIL media overlay and the media:* metadata
are hand-built (ebooklib's EpubSMIL is a content carrier only)."""
from reader import ids   # noqa: F401 (kept for parity; ids used by callers)

def clock(seconds):
    h = int(seconds // 3600); m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:06.3f}"

def section_duration(section_id, timing):
    ends = [c["end"] for c in timing["clips"].values() if c["section"] == section_id]
    return max(ends) if ends else 0.0

_SMIL = """<?xml version="1.0" encoding="utf-8"?>
<smil xmlns="http://www.w3.org/ns/SMIL" xmlns:epub="http://www.idpf.org/2007/ops" version="3.0">
<body>
<seq id="seq-{sec}" epub:textref="{xhtml}" epub:type="chapter">
{pars}
</seq>
</body></smil>"""

def build_smil(section_id, xhtml_href, audio_href, timing):
    pars = []
    clips = [(cid, c) for cid, c in timing["clips"].items() if c["section"] == section_id]
    for cid, c in clips:
        pars.append(
            f'<par id="par-{cid}">'
            f'<text src="{xhtml_href}#{cid}"/>'
            f'<audio src="{audio_href}" clipBegin="{clock(c["begin"])}" '
            f'clipEnd="{clock(c["end"])}"/></par>')
    return _SMIL.format(sec=section_id, xhtml=xhtml_href, pars="\n".join(pars))
