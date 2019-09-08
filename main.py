import json
import unittest
import argparse
from converter.generateInputFile import generateTestInput
from converter.specLoader import loadSpec
from converter.converterToCsv import FixedWidthToCsv



# if __name__ == "__main__":

generateTestInput()

colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = loadSpec("spec.json")
with open("test-input2.txt",'r',encoding=fixedWidthEncoding) as inputFile,\
    open("test2.csv",'w',encoding=delimitedEncoding, newline='') as outputFile:

    aa = FixedWidthToCsv(inputFile,outputFile,"spec.json")
    aa.toCsvFile()




