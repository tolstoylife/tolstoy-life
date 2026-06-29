from reader.build_xhtml import render_section_xhtml
from reader.build_epub import page_list_nav

SEG = {"work":"the-great-sin","version":"en-1905","spine":"ru","notes":[],
  "sections":[{"id":"sec-1","heading":"Part I","headingSpeech":"Part One.",
    "paragraphs":[{"id":"p-1-1","pss":"36:206","sentences":[
        {"id":"p-1-1-s1","display":"A.","speech":"A."}]}]}]}

def test_pagebreak_anchor_in_xhtml():
    html = render_section_xhtml(SEG, "sec-1", "The Great Sin", "en")
    assert 'epub:type="pagebreak"' in html
    assert 'aria-label="PSS 36:206"' in html

def test_page_list_nav():
    nav = page_list_nav(SEG)
    assert 'epub:type="page-list"' in nav
    assert "PSS 36:206" in nav
    assert "#page-36-206" in nav
