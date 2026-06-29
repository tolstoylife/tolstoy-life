# reader/paragraph_ids.py
"""Add p-{section}-{n} ids to rendered HTML <p> elements, numbered per <h2>
section, matching reader.ids so web annotations share the EPUB's coordinates.
A regex post-processor over the HTML string — no extra dependency."""
import re
from reader import ids

def add_paragraph_ids(html_fragment):
    section = [0]; n = [0]
    def repl(m):
        tag = m.group(0)
        if tag.lower().startswith("<h2"):
            section[0] += 1; n[0] = 0
            return tag
        if "id=" in tag:                       # leave explicit ids alone
            return tag
        n[0] += 1
        return f'<p id="{ids.paragraph_id(section[0], n[0])}"' + tag[2:]
    return re.sub(r"<h2\b[^>]*>|<p\b[^>]*>", repl, html_fragment)
