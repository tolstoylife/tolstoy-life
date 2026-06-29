from reader import validate

def test_skips_gracefully_when_absent(monkeypatch):
    monkeypatch.setattr(validate.shutil, "which", lambda _: None)
    ok, msg = validate.epubcheck("nonexistent.epub")
    assert ok is True and "skipped" in msg
    ok, msg = validate.ace("nonexistent.epub", "/tmp/ace")
    assert ok is True and "skipped" in msg
