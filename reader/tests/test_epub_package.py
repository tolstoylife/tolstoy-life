import zipfile
from reader.build_epub import build_epub
from reader.segment import segment

TIMING = {
  "audio": {"sec-1": "audio/the-great-sin.sec-1.m4a"},
  "clips": {"sec-1": {"section":"sec-1","begin":0.0,"end":1.1},
            "p-1-1-s1": {"section":"sec-1","begin":1.55,"end":4.97},
            "p-1-1-s2": {"section":"sec-1","begin":5.4,"end":7.1},
            "p-1-2-s1": {"section":"sec-1","begin":7.5,"end":9.0},
            "p-1-2-s2": {"section":"sec-1","begin":9.4,"end":11.0}}}
META = {"title":"A Great Iniquity","author":"Leo Tolstoy","lang":"en",
        "source":"PSS vol. 36","translator":"V. Tchertkoff & I. Mayo","date":"1905",
        "pss_pages":{"sec-1":"PSS 36:206"}}

def test_epub_is_written_and_has_overlay(tmp_path):
    seg = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    # the test audio file need not exist for packaging; create a stub
    (tmp_path / "audio").mkdir()
    (tmp_path / "audio" / "the-great-sin.sec-1.m4a").write_bytes(b"\x00")
    out = build_epub(seg, TIMING, str(tmp_path / "out.epub"), META,
                     audio_root=str(tmp_path))
    z = zipfile.ZipFile(out)
    names = z.namelist()
    assert any(n.endswith(".smil") for n in names)
    opf = next(n for n in names if n.endswith(".opf"))
    content = z.read(opf).decode()
    assert "media:duration" in content
    assert "media:active-class" in content
    assert "schema:accessMode" in content or "accessMode" in content
    assert "dcterms:conformsTo" in content


def test_smil_srcs_resolve_to_real_files(tmp_path):
    """Every SMIL text/audio src must resolve to a real file in the zip. A wrong
    relative path (missing ../text/) keeps the fragment ids valid but points at a
    nonexistent file, which silently kills read-along in Apple Books."""
    import re, posixpath
    seg = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    (tmp_path / "audio").mkdir()
    (tmp_path / "audio" / "the-great-sin.sec-1.m4a").write_bytes(b"\x00")
    out = build_epub(seg, TIMING, str(tmp_path / "out.epub"), META,
                     audio_root=str(tmp_path))
    z = zipfile.ZipFile(out)
    names = set(z.namelist())
    smils = [n for n in names if n.endswith(".smil")]
    assert smils, "no SMIL in package"
    for n in smils:
        base = posixpath.dirname(n)
        for src in re.findall(r'src="([^"]+)"', z.read(n).decode()):
            full = posixpath.normpath(posixpath.join(base, src.split("#")[0]))
            assert full in names, f"{n}: src {src!r} -> {full} missing from epub"


def test_active_class_backed_by_css_and_valid_contributor(tmp_path):
    """EPUBCheck regressions: a declared media:active-class needs a CSS that the
    content doc actually LINKS and that defines it (CSS-030 — ebooklib strips
    inline <link>s, so the link must be registered via its API), and the
    translator role must use the marc:relators refines pattern, not a bare role=
    attribute on dc:contributor (RSC-005)."""
    import re, posixpath
    seg = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    (tmp_path / "audio").mkdir()
    (tmp_path / "audio" / "the-great-sin.sec-1.m4a").write_bytes(b"\x00")
    out = build_epub(seg, TIMING, str(tmp_path / "out.epub"), META,
                     audio_root=str(tmp_path))
    z = zipfile.ZipFile(out)
    names = z.namelist()
    opf = next(z.read(n).decode() for n in names if n.endswith(".opf"))
    assert 'scheme="marc:relators"' in opf       # translator role the EPUB3 way
    assert "<dc:contributor role=" not in opf    # ...not the invalid attribute

    if "media:active-class" in opf:
        for doc_name in [n for n in names if n.startswith("EPUB/text/") and n.endswith(".xhtml")]:
            doc = z.read(doc_name).decode()
            hrefs = [re.search(r'href="([^"]+)"', tag).group(1)
                     for tag in re.findall(r"<link[^>]*>", doc)
                     if "stylesheet" in tag and re.search(r'href="([^"]+)"', tag)]
            assert hrefs, f"{doc_name}: head links no stylesheet"
            defines = []
            for h in hrefs:
                target = posixpath.normpath(posixpath.join(posixpath.dirname(doc_name), h))
                if target in names:
                    defines.append("-epub-media-overlay-active" in z.read(target).decode())
            assert any(defines), f"{doc_name}: no linked CSS defines the active-class"
