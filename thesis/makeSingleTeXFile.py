#! /usr/bin/python3

import argparse
import logging
import re
import sys
import time

# https://zapier.com/engineering/profiling-python-boss/
def printTimeForFunction(f):
    def f_timer(*args, **kwargs):
        start = time.monotonic()
        result = f(*args, **kwargs)
        end = time.monotonic()
        logging.getLogger().info("%s %s.tex --> %.4fs" % (f.__name__, kwargs["texfile"], end - start))
        return result
    return f_timer

@printTimeForFunction
def process(texfile, outputFile):
    with open("%s.tex" % texfile, 'r') as texFile:
        for line in texFile:
            parts = line.split('%')
            inputFile = re.search("(\\\\input{)(?P<input>.*?)(})", parts[0])
            includeFile = re.search("(\\\\\include{)(?P<include>.*?)(})", parts[0])
            if inputFile:
                process(texfile=inputFile.group("input"), outputFile=outputFile)
            elif includeFile:
                process(texfile=includeFile.group("include"), outputFile=outputFile)
            else:
                outputFile.write(bytes(line, 'UTF-8'))

def createLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def main():
    parser = argparse.ArgumentParser(description='Produces single TeX file by including referenced Tex files.')
    parser.add_argument('--inputFile', type=str, help='file with input/include (w/o .tex)')
    parser.add_argument('--outputFile', type=str, help='target file (w/o .tex)')
    args = parser.parse_args()

    assert args.inputFile != None
    assert args.outputFile != None

    createLogger()

    with open(args.outputFile + ".tex", 'wb') as outputFile:
        process(texfile=args.inputFile, outputFile=outputFile)

if __name__ == "__main__":
    main()
