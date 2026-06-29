from reader.build_epub import clock, build_smil, section_duration

TIMING = {
  "audio": {"sec-1": "audio/the-great-sin.sec-1.m4a"},
  "clips": {
    "sec-1":    {"section": "sec-1", "begin": 0.0,  "end": 1.10},
    "p-1-1-s1": {"section": "sec-1", "begin": 1.55, "end": 4.97}}}

def test_clock_format():
    assert clock(1.1) == "0:00:01.100"
    assert clock(3661.5) == "1:01:01.500"

def test_section_duration_is_last_end():
    assert section_duration("sec-1", TIMING) == 4.97

def test_smil_has_par_per_clip_with_clips():
    smil = build_smil("sec-1", "text/sec-1.xhtml", "audio/the-great-sin.sec-1.m4a", TIMING)
    assert smil.count("<par") == 2
    assert 'epub:textref="text/sec-1.xhtml#p-1-1-s1"' in smil or \
           'src="text/sec-1.xhtml#p-1-1-s1"' in smil
    assert 'clipBegin="0:00:01.550"' in smil
    assert 'clipEnd="0:00:04.970"' in smil
    import xml.dom.minidom as m; m.parseString(smil)
