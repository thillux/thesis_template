# thesis_template

German latex templates for thesis writing at Ilmenau University of Technology, tailored for computer science students.

* all files encoded as UTF-8
* based on KOMA-Script classes

## Prerequisites

* TeX Live / MiKTeX / your favourite LaTeX distribution
* Python 3
* SCons

## Usage

```bash
 scons [expose|letter|slides|thesis]
```

## Subfolders

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
  * Carsten Hahn
  * Lennard Pfennig
  * Markus Theil
