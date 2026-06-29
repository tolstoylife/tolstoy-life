# reader/validate.py
"""EPUBCheck + ACE by DAISY gates. Skip-with-warning if the tool isn't installed
(don't hard-fail the proof build for a missing validator)."""
import shutil, subprocess

def epubcheck(path):
    exe = shutil.which("epubcheck")
    if not exe:
        return True, "skipped: epubcheck not found (install: brew install epubcheck)"
    p = subprocess.run([exe, path], capture_output=True, text=True)
    return p.returncode == 0, (p.stdout + p.stderr)

def ace(path, out_dir):
    exe = shutil.which("ace")
    if not exe:
        return True, "skipped: ace not found (install: npm i -g @daisy/ace)"
    p = subprocess.run([exe, "-o", out_dir, path], capture_output=True, text=True)
    return p.returncode == 0, (p.stdout + p.stderr)
