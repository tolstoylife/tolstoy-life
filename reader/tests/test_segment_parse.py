from reader.segment import parse, heading_speech

MD = open("reader/tests/fixtures/mini.en-1905.md").read()

def test_heading_speech():
    assert heading_speech("Part I") == "Part One."
    assert heading_speech("Part IV") == "Part Four."
    assert heading_speech("Introduction") == "Introduction."

def test_parse_structure():
    doc = parse(MD)
    assert len(doc["sections"]) == 1
    sec = doc["sections"][0]
    assert sec["id"] == "sec-1"
    assert sec["heading"] == "Part I"
    assert sec["headingSpeech"] == "Part One."
    assert [p["id"] for p in sec["paragraphs"]] == ["p-1-1", "p-1-2"]

def test_parse_sentence_ids_and_text():
    sec = parse(MD)["sections"][0]
    s = sec["paragraphs"][0]["sentences"]
    assert [x["id"] for x in s] == ["p-1-1-s1", "p-1-1-s2"]
    assert s[0]["display"] == "The other day I was walking along the high road to Tula."

def test_parse_resolves_marks_in_display():
    sec = parse(MD)["sections"][0]
    p2 = sec["paragraphs"][1]["sentences"]
    # wikilink label kept, footnote marker kept in display, stripped in speech
    assert "[[old woman]]" not in p2[1]["display"]
    assert "old woman" in p2[1]["display"]
    assert "[^1]" in p2[0]["display"]
    assert "[^1]" not in p2[0]["speech"]

def test_parse_collects_notes():
    notes = parse(MD)["notes"]
    assert notes == [{"id": "note-1", "label": "1", "html": "A cow without milk."}]
