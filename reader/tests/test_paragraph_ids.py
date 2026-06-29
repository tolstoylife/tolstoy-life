from reader.paragraph_ids import add_paragraph_ids

def test_numbers_paragraphs_per_section():
    html = "<h2>Part I</h2><p>One.</p><p>Two.</p><h2>Part II</h2><p>Three.</p>"
    out = add_paragraph_ids(html)
    assert 'id="p-1-1"' in out
    assert 'id="p-1-2"' in out
    assert 'id="p-2-1"' in out

def test_preamble_paragraph_before_first_heading_is_section_0():
    html = "<p>Intro.</p><h2>Part I</h2><p>Body.</p>"
    out = add_paragraph_ids(html)
    assert 'id="p-0-1"' in out      # before any heading
    assert 'id="p-1-1"' in out

def test_leaves_existing_ids_alone():
    html = '<p id="keep">x</p>'
    assert add_paragraph_ids(html) == '<p id="keep">x</p>'
