from reader.segment import resolve_reading_text, split_sentences

def test_resolve_criticmarkup():
    assert resolve_reading_text("I knew {--this--} the woman") == "I knew the woman"
    assert resolve_reading_text("a {++very ++}old woman") == "a very old woman"
    assert resolve_reading_text("the {~~horse~>cow~~}") == "the cow"
    assert resolve_reading_text("text {>>editor cut this<<}here") == "text here"
    assert resolve_reading_text("a {==dropped==} word") == "a dropped word"

def test_resolve_keeps_wikilink_label_and_footnote():
    assert resolve_reading_text("the [[old woman]] spoke") == "the old woman spoke"
    assert resolve_reading_text("a cow.[^1] I knew her.") == "a cow.[^1] I knew her."

def test_split_sentences_basic():
    out = split_sentences("First one. Second one! Third?")
    assert out == ["First one.", "Second one!", "Third?"]

def test_split_protects_decimals():
    out = split_sentences("It cost 1.40 rubles. That is dear.")
    assert out == ["It cost 1.40 rubles.", "That is dear."]
