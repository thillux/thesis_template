# -*- coding: utf-8 -*-

EnsurePythonVersion(2, 7)
EnsureSConsVersion(2, 3)

import multiprocessing
import os

SetOption('num_jobs', multiprocessing.cpu_count())
print("scons: running with {} cores".format(GetOption('num_jobs')))

########################################

# global defines

PATH = "/usr/local/bin:/opt/bin:/bin:/usr/bin:/usr/texbin"

########################################

# environments

texEnv = Environment(ENV = { "PATH" : PATH }, PDFLATEXFLAGS='-synctex=1')
defaultTargets = []

########################################

# slides

pdfOutputSlides = SConscript('slides/SConscript', exports="texEnv")
defaultTargets.append(pdfOutputSlides)

########################################

# thesis
pdfOutputThesis = SConscript('thesis/SConscript', exports="texEnv")
defaultTargets.append(pdfOutputThesis)

########################################

# expose
pdfOutputExpose = SConscript('expose/SConscript', exports="texEnv")
defaultTargets.append(pdfOutputExpose)

########################################

# extension
pdfOutputLetter = SConscript('letter/SConscript', exports="texEnv")
defaultTargets.append(pdfOutputLetter)

########################################

# default targets

Default(defaultTargets)

########################################

# vim: set filetype=python
