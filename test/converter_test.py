import json
import unittest
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from converter.converterToCsv import FixedWidthToCsv
from converter.specLoader import loadSpec

# from ..converter.converterToCsv import FixedWidthToCsv

class ConverterTest(unittest.TestCase):

        def __init__(self):
            print(888888888888888888)
            self.colNames, self.offsets, self.fixedWidthEncoding, self.includeHeader, self.delimitedEncoding = loadSpec('spec.json')
            # with open("..\\testInput.txt", 'r', encoding=self.fixedWidthEncoding) as inputFile, \
            #         open("testTest.txt", 'w', encoding=self.delimitedEncoding, newline='') as outputFile:
            #     self.converter = FixedWidthToCsv(inputFile, outputFile, "spec.json")

            self.inputFile = open("..\\testInput.txt", 'r', encoding=self.fixedWidthEncoding)
            self.outputFile = open("testTest.txt", 'w', encoding=self.delimitedEncoding, newline='')
            self.converter = FixedWidthToCsv(self.inputFile, self.outputFile, "spec.json")

        def readlineTest(self):
            row = {}
            row['f1'] = 'f1111'
            row['f2'] = 'f22222222222'
            row['f3'] = 'f33'
            row['f4'] = 'f4'
            row['f5'] = 'f555555555555'
            row['f6'] = 'f666666'
            row['f7'] = 'f777777777'
            row['f8'] = 'f888888888888'
            row['f9'] = 'f9999999999999999999'
            row['f10'] = 'f100000000000'
            print(888888888888888888)
            colNames = self.converter.colNames
            index = 0
            for line in self.inputFile:
                for head in range(len(self.colNames)):
                    index += 1
                    colName = "f"+str(index)
                    rowDict = self.converter.readRow(line)
                    self.assertEqual(row[colName], rowDict[colName])
                break

if __name__ == "__main__":
    print(98899999)
    unittest.main()

