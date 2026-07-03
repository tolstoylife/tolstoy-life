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

def test_respell_kvass():
    assert to_speech("Just enough for Kvas.") == "Just enough for quahss."

def test_money_spelled_out():
    assert "one dollar forty a day" in to_speech("work for an average of $1.40 a day, it is no wonder")

def test_professions_list_gets_full_stops():
    out = to_speech('These men—the nobles, merchants, Government officials, doctors, '
                    'engineers, professors, teachers, artists, students, advocates, '
                    'chiefly townspeople, the so-called "intellectuals"—are now in Russia')
    assert "the nobles. Merchants." in out
    assert "Chiefly townspeople. The so-called" in out
