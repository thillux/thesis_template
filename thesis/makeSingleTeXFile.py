#! /usr/bin/python3

import argparse
import logging
import re
import sys
import time

# https://zapier.com/engineering/profiling-python-boss/
def printTimeForTeXInclude(f):
    def f_timer(*args, **kwargs):
        start = time.monotonic()
        result = f(*args, **kwargs)
        end = time.monotonic()
        logging.getLogger().info("processed %s.tex --> %.4fs" % (kwargs["texfile"], end - start))
        return result
    return f_timer

def printTimeForFunction(f):
    def f_timer(*args, **kwargs):
        start = time.monotonic()
        result = f(*args, **kwargs)
        end = time.monotonic()
        logging.getLogger().info("time for fn: %s --> %.4fs" % (f.__name__, end - start))
        return result
    return f_timer

@printTimeForTeXInclude
def process(texfile, outputFile):
    with open("%s.tex" % texfile, 'r', encoding="utf-8") as texFile:
        lineNumber = 1
        for line in texFile:
            parts = line.split('%')
            inputFile = re.search("(\\\\input{)(?P<input>.*?)(})", parts[0])
            includeFile = re.search("(\\\\\include{)(?P<include>.*?)(})", parts[0])
            if inputFile:
                logging.getLogger().info("input %s.tex:%i <-- %s.tex" % (texfile, lineNumber, inputFile.group("input")))
                process(texfile=inputFile.group("input"), outputFile=outputFile)
            elif includeFile:
                logging.getLogger().info("include %s.tex:%i <-- %s.tex" % (texfile, lineNumber, includeFile.group("include")))
                process(texfile=includeFile.group("include"), outputFile=outputFile)
            else:
                outputFile.write(line)
            lineNumber += 1

@printTimeForFunction
def createLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

@printTimeForFunction
def main():
    parser = argparse.ArgumentParser(description='Produces single TeX file by including referenced Tex files.')
    parser.add_argument('--inputFile', type=str, help='file with input/include (w/o .tex)')
    parser.add_argument('--outputFile', type=str, help='target file (w/o .tex)')
    args = parser.parse_args()

    assert args.inputFile != None
    assert args.outputFile != None

    createLogger()

    with open(args.outputFile + ".tex", 'w', encoding="utf-8") as outputFile:
        process(texfile=args.inputFile, outputFile=outputFile)

if __name__ == "__main__":
    main()
