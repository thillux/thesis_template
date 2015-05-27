#!/bin/sh

./timeAdjust.py zeitplan.json zeitplan.tex
latexmk expose.tex -bibtex -pdf
