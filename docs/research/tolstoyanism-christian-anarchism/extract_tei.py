#!/usr/bin/env python3
"""Extract plain prose from a tolstoydigital-TEI XML file.

Usage:
  extract_tei.py <path-to-xml>            # prints full body text + metadata
  extract_tei.py <xml> <substring>        # prints paragraphs containing substring
"""
import re
import sys
from lxml import etree

NS = {
    "t": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace",
}

SUPERSCRIPT = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def normalise_paragraph(p):
    """Walk a <p> element and return its visible Russian prose, resolving <choice>/<sic>/<corr>."""
    parts = []
    for node in p.iter():
        tag = etree.QName(node).localname

        # Editorial: <choice> contains <sic> (original) and <corr> (corrected/expanded).
        # When we hit <choice> we'll process its children explicitly and skip recursion.
        # Easier approach: only collect text from <corr>, skip <sic>; skip <note> bodies entirely.
        if tag == "note":
            # Skip note text — these are footnote bodies, not Tolstoy's prose.
            node.clear()  # destructive but we don't reuse the tree
            continue

    # Re-iterate cleanly: prefer <corr> over <sic>, drop <note>.
    text = []

    def walk(node):
        tag = etree.QName(node).localname
        if tag == "note":
            return
        if tag == "choice":
            corr = node.find("t:corr", NS)
            if corr is not None:
                walk(corr)
            return
        if tag == "sic":
            return  # sibling of <corr>, already handled above
        # Footnote anchors. Print PSS renders these as superscript digits bound
        # to the preceding word. The TEI corpus uses two markups inconsistently:
        #   <hi>1</hi>                     (Eltzbacher, Sacy letters)
        #   <ref target="#note1">1</ref>   (Schmitt, Stakhovich, Germogen, …)
        # Both, when digit-only, get the same superscript treatment.
        is_hi_anchor = (
            tag == "hi" and not node.get("style") and (node.text or "").strip().isdigit()
        )
        is_ref_anchor = (
            tag == "ref"
            and (node.get("target") or "").startswith("#note")
            and (node.text or "").strip().isdigit()
        )
        if is_hi_anchor or is_ref_anchor:
            t = node.text.strip()
            # eat any trailing whitespace already in the buffer so the
            # superscript binds to the preceding word
            while text and text[-1] and text[-1][-1:].isspace():
                text[-1] = text[-1].rstrip()
                if not text[-1]:
                    text.pop()
            text.append(t.translate(SUPERSCRIPT))
            return  # parent will handle node.tail
        if node.text:
            text.append(node.text)
        for child in node:
            walk(child)
            if child.tail:
                text.append(child.tail)

    walk(p)
    out = " ".join("".join(text).split())
    # Collapse space-before-punctuation produced by inline <title>/<emph> tails.
    out = re.sub(r"\s+([.,;:!?»])", r"\1", out)
    out = re.sub(r"([«])\s+", r"\1", out)
    # Repair structural collisions where TEI markup eats a boundary character:
    #   <name>(Paul Eltzbacher)</name>.1900 г.   →   "). 1900 г."
    out = re.sub(r"\)\.(\d)", r"). \1", out)
    #   ".1901г. Июля 28"   →   ". 1901 г. Июля 28"   (rare TEI source quirk)
    out = re.sub(r"(\d{4})г\.", r"\1 г.", out)
    return out


def extract(path):
    tree = etree.parse(path)
    root = tree.getroot()

    bibl = root.find(".//t:title[@type='bibl']", NS)
    main_title = root.find(".//t:title[@type='main']", NS)
    sub_title = root.find(".//t:title[@type='sub']", NS)
    file_id_el = root.find(".//t:title[@xml:id]", NS)

    bibl_text = bibl.text.strip() if bibl is not None and bibl.text else ""
    title_text = ""
    if main_title is not None and main_title.text:
        title_text = main_title.text.strip()
    if sub_title is not None and sub_title.text:
        title_text = (title_text + " " + sub_title.text.strip()).strip()

    file_id = ""
    if file_id_el is not None:
        file_id = file_id_el.get("{http://www.w3.org/XML/1998/namespace}id", "")

    paragraphs = []
    body = root.find(".//t:body", NS)
    if body is None:
        return file_id, title_text, bibl_text, []

    def inside_note(el):
        cur = el.getparent()
        while cur is not None and cur is not body:
            if etree.QName(cur).localname in ("note", "noteGrp"):
                return True
            cur = cur.getparent()
        return False

    # Collect openers and paragraphs in document order; skip any wrapped in editorial <note>.
    for el in body.iter():
        tag = etree.QName(el).localname
        if tag in ("opener", "p", "closer", "head"):
            if inside_note(el):
                continue
            txt = normalise_paragraph(el)
            if txt:
                paragraphs.append((tag, txt))
    return file_id, title_text, bibl_text, paragraphs


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    needle = sys.argv[2] if len(sys.argv) > 2 else None

    file_id, title, bibl, paragraphs = extract(path)
    print(f"# {title}")
    print(f"# id: {file_id}")
    print(f"# bibl: {bibl}")
    print()
    for tag, txt in paragraphs:
        if needle and needle.lower() not in txt.lower():
            continue
        prefix = f"[{tag}] " if tag != "p" else ""
        print(prefix + txt)
        print()


if __name__ == "__main__":
    main()
