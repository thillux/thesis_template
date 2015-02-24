#!/bin/sh

curl http://ftp.uni-erlangen.de/mirrors/ripe.net/rfc/tar/RFC-all.tar.gz -O
tar xzf RFC-all.tar.gz

rm -rf a rfc1305.tar pdf  ps  txt
mkdir -p txt ps pdf

mv *.txt txt
mv *.pdf pdf
mv *.ps ps
