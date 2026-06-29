from reader import ids

def test_id_shapes():
    assert ids.section_id(1) == "sec-1"
    assert ids.paragraph_id(1, 12) == "p-1-12"
    assert ids.sentence_id("p-1-12", 2) == "p-1-12-s2"
    assert ids.typed_id("fig", 4, 1) == "fig-4-1"
    assert ids.typed_id("bq", 4, 2) == "bq-4-2"
    assert ids.note_id(1) == "note-1"
    assert ids.noteref_id(1) == "noteref-1"
