## Program: Convert fixed width file to csv
## version 1.0.0
## Author: Dejun Xiang
## Date: 08/09/2019

from csv import DictWriter
from converter.specLoader import loadSpec,readRow

class FixedWidthToCsv():

    def __init__(self,inputFile,outputFile,specFile):

        self.inputFile = inputFile
        self.outputFile = outputFile
        self.specFile = specFile
        self.colNames,self.offsets, _ ,self.includeHeader, _ = loadSpec(specFile)

    def toCsvFile(self):
        writer = DictWriter(self.outputFile,fieldnames = self.colNames)
        # be careful, 'True' is a string not a boolean value
        if self.includeHeader == 'True':
            writer.writeheader()

        for row in self.inputFile:
            rowDict = readRow(row, self.colNames, self.offsets)
            writer.writerow(rowDict)