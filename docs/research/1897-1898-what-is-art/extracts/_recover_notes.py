#!/usr/bin/env python3
"""One-off: recover Tolstoy's authorial inline <note> footnotes from the
What Is Art? TEI (which extract_tei.py strips), resolving <choice> to the
modern-orthography <reg>/<corr> reading. Writes byte-faithful note text so
the famous self-condemnation footnote (PSS 30) can be cited + verify_quotes'd.
"""
import sys
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
PATH = "primary-sources/tolstoydigital-TEI/texts/works/v30_027_203_Chto_takoe_iskusstvo.xml"


def text_of(el):
    """Serialise element text, resolving choice->reg/corr, dropping note-internal markers."""
    parts = []

    def walk(node):
        tag = etree.QName(node).localname
        if tag == "choice":
            reg = node.find("t:reg", NS)
            corr = node.find("t:corr", NS)
            pick = reg if reg is not None else corr
            if pick is not None:
                parts.append(pick.text or "")
            if node.tail:
                parts.append(node.tail)
            return
        if node.text:
            parts.append(node.text)
        for child in node:
            walk(child)
        if node.tail:
            parts.append(node.tail)

    # don't include the note's own .tail
    if el.text:
        parts.append(el.text)
    for child in el:
        walk(child)
    return "".join(parts)


def main():
    tree = etree.parse(PATH)
    out = []
    for note in tree.iter("{http://www.tei-c.org/ns/1.0}note"):
        resp = note.get("resp", "")
        txt = " ".join(text_of(note).split())
        if not txt:
            continue
        out.append((resp, txt))
    print("# Authorial/inline notes recovered from v30_027_203_Chto_takoe_iskusstvo.xml")
    print("# (extract_tei.py strips inline <note>; this recovers them with --choice=reg semantics)")
    print("# resp attribute shown in brackets; verify against PSS Tom 30 PDF.")
    print()
    for resp, txt in out:
        tag = f"[{resp}] " if resp else ""
        print(tag + txt)
        print()


if __name__ == "__main__":
    main()
