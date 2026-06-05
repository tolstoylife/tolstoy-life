#!/usr/bin/env python3
"""Reconstruct TEI letter/diary body text resolving <choice> by preferring
<reg> (regularized orthography) then <corr>, then <orig>/<sic>. Fixes the
extract_tei.py pre-reform <choice><orig>/<reg> gap for 1880-81 letters.
Usage: _reg_extract.py <xml>  -> prints paragraphs (one per source <p>)."""
import sys, re
import xml.etree.ElementTree as ET

NS = "{http://www.tei-c.org/ns/1.0}"
def ln(t): return t.split("}")[-1]

def walk(el, out):
    tag = ln(el.tag)
    if tag == "choice":
        pick = el.find(f"{NS}reg")
        if pick is None: pick = el.find(f"{NS}corr")
        if pick is None: pick = el.find(f"{NS}orig")
        if pick is None: pick = el.find(f"{NS}sic")
        if pick is not None:
            if pick.text: out.append(pick.text)
            for c in pick: walk(c, out)
        if el.tail: out.append(el.tail)
        return
    if tag in ("note", "pb", "ref"):
        if el.tail: out.append(el.tail)
        return
    if el.text: out.append(el.text)
    for c in el: walk(c, out)
    if el.tail: out.append(el.tail)

tree = ET.parse(sys.argv[1])
root = tree.getroot()
body = root.find(f".//{NS}body")
for p in body.iter(f"{NS}p"):
    out = []
    # only direct text of this <p>, not nested <p>; TEI letters rarely nest <p>
    if p.text: out.append(p.text)
    for c in p: walk(c, out)
    txt = re.sub(r"\s+", " ", "".join(out)).strip()
    txt = re.sub(r"\s+([,.;:!?»])", r"\1", txt)
    txt = re.sub(r"([«])\s+", r"\1", txt)
    if txt:
        print(txt)
        print()
