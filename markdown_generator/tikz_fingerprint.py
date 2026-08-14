#!/usr/bin/env python3
r"""Fingerprint everything that determines the rendered tikz PNGs for a deck.

`build_site.sh --no-tikz` reuses already-rendered diagrams. Deciding when that is
safe by mtime is both too strict and too loose: Dropbox touches files without
changing them (false alarm, ~10 min of xelatex for nothing), and a PNG count
check alone misses a diagram edited in place (silently ships a stale picture).

The exact condition is content, not time. render_slide_tikz.render() feeds
xelatex exactly three things from the deck -- the \definecolor lines, the
usetikzlibrary list, and the \begin{tikzpicture} blocks -- wrapped in a TEMPLATE
that lives in the script itself. Hash those four and you have a fingerprint that
changes if and only if the PNGs would.

Usage:  python3 tikz_fingerprint.py <deck.md>     -> prints the hex digest
"""
import hashlib
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render_slide_tikz as R  # noqa: E402


def fingerprint(src_path):
    src = open(src_path, encoding="utf-8").read()
    colors, libs, pics = R.extract(src)
    h = hashlib.sha256()
    # The renderer's own template is an input too: change the preamble and every
    # PNG changes while the deck does not.
    h.update(open(R.__file__, "rb").read())
    for part in (colors, libs, *pics):
        h.update(b"\x00")
        h.update(part.encode("utf-8"))
    return h.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: tikz_fingerprint.py <deck.md>")
    print(fingerprint(sys.argv[1]))
