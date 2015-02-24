#!/usr/bin/bash

# source: http://tm.uka.de/~bless/bibrfcindex.html

rfcIndexURL='http://www.rfc-editor.org/in-notes/rfc-index.xml'
rfcIndexFilename='rfc-index.xml'

echo "Download $rfcIndexFilename"
curl "-#" -o $rfcIndexFilename $rfcIndexURL

echo "Create bibtex file"
xsltproc rfcxmlindex2bibtex.xslt rfc-index.xml | \
         sed -e 's/\([_&%#$]\)/\\\1/g' -e '/author=/s/\([^ ]*\) \(3rd\|Jr\.\)/\{\1 \2\}/g' \
         > rfc.bib
