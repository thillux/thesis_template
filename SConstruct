# -*- coding: utf-8 -*-

EnsurePythonVersion(2, 7)
EnsureSConsVersion(2, 3)

import os

########################################

# global defines

PATH = "/usr/local/bin:/opt/bin:/bin:/usr/bin:/usr/texbin"

########################################

# environments

texEnv = Environment(ENV = { "PATH" : PATH }, PDFLATEXFLAGS='-synctex=1')

########################################

# slides

pdfOutputSlides = SConscript('slides/SConscript', exports="texEnv")

########################################

# thesis
pdfOutputThesis = SConscript('thesis/SConscript', exports="texEnv")

########################################

# default targets

Default(pdfOutputSlides, pdfOutputThesis)

########################################

# vim: set filetype=python
