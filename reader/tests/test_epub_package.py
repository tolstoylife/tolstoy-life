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
