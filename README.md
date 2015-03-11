# thesis_template

German latex templates for thesis writing at Ilmenau University of Technology, tailored for computer science students.

* all files encoded as UTF-8
* based on KOMA-Script classes

## Prerequisites

### General
* [TeX Live](https://www.tug.org/texlive/) / [MiKTeX](http://miktex.org/) / your favourite LaTeX distribution
* [Python 3](https://docs.python.org/3/)
* [SCons](http://www.scons.org/)

### Generating RFC BibTeX File 
* [xsltproc](http://xmlsoft.org/XSLT/xsltproc2.html)
* [curl](http://curl.haxx.se/)

### Downloading RFCs
* [curl](http://curl.haxx.se/)

## Usage

```bash
 scons [expose|letter|slides|thesis]
```

## Contents

### expose
Document for the first stage of your thesis project. Write down your schedule and intended methods here.  

* based on scrartcl
* adjustable schedule [just edit a JSON file]
* some simple includes for math formula

### letter
Letter template which can be used, if you need to request something with regard to your thesis.

* based on scrlttr2

### thesis

* nice titlepage
* uses TikZ for colored boxes

### slides

* beamer-based
* no navigation symbols
* separate slide numbers for  backup slides (like 35/20)

## Contributors
* Martin Backhaus
* Carsten Hahn
* René Köllmer
* Lennard Pfennig
* Markus Theil

## Credits

* RFC bib file generator script from [Dr. Roland Bless](http://telematics.tm.kit.edu/staff_bless.php) in scripts/rfcs/bibtex
* small snippets from sites like [Stack Overflow](https://www.stackoverflow.com/) are linked inside the respective files

