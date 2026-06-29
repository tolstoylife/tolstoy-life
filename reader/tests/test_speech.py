from reader.speech import to_speech

def test_semicolon_before_conjunction_becomes_comma():
    assert to_speech("pahать time; and the horse is gone") == "pahать time, and the horse is gone"

def test_bare_semicolon_becomes_full_stop():
    assert to_speech("one thing; another follows") == "one thing. Another follows"

def test_respell_known_words():
    assert "Labooshair" in to_speech("the MP Labouchere spoke")
    assert "Yasnaya Polyahna" in to_speech("near Yasnaya Poliana")

def test_strips_footnote_marker():
    assert to_speech("leading a cow.[^1] I knew her.") == "leading a cow. I knew her."

def test_ellipsis_normalised():
    assert to_speech("well... maybe") == "well… maybe"
