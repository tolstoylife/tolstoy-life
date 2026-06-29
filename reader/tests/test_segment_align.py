import json, subprocess, sys
import pytest
from reader.segment import segment, parse

def test_segment_full_shape():
    doc = segment("reader/tests/fixtures/mini.en-1905.md",
                  version="en-1905", work="the-great-sin")
    assert doc["work"] == "the-great-sin"
    assert doc["version"] == "en-1905"
    assert doc["spine"] == "ru"
    assert doc["sections"][0]["paragraphs"][0]["id"] == "p-1-1"

def test_alignment_passes_when_parallel():
    spine = parse(open("reader/tests/fixtures/mini.ru.md").read())
    # should not raise — both fixtures have 1 section, 2 paragraphs
    segment("reader/tests/fixtures/mini.en-1905.md",
            version="en-1905", work="the-great-sin", spine_doc=spine)

def test_alignment_fails_on_mismatch():
    fake_spine = {"sections": [{"id": "sec-1", "paragraphs": [{"id": "p-1-1"}]}],
                  "notes": []}  # only 1 paragraph
    with pytest.raises(ValueError, match="paragraph count"):
        segment("reader/tests/fixtures/mini.en-1905.md",
                version="en-1905", work="the-great-sin", spine_doc=fake_spine)

def test_cli_writes_json(tmp_path):
    out = tmp_path / "seg.json"
    subprocess.run([sys.executable, "-m", "reader.segment",
                    "reader/tests/fixtures/mini.en-1905.md",
                    "--version", "en-1905", "--work", "the-great-sin",
                    "-o", str(out)], check=True)
    doc = json.loads(out.read_text())
    assert doc["version"] == "en-1905"
