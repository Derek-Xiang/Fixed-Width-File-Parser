from csv import DictWriter
from converter.specLoader import loadSpec
import json

class FixedWidthToCsv():

    def __init__(self,inputFile,outputFile,specFile):

        self.inputFile = inputFile
        self.outputFile = outputFile
        self.specFile = specFile
        self.colNames,self.offsets,self.fixedWidthEncoding,self.includeHeader,self.delimitedEncoding = loadSpec(specFile)

    def toCsvFile(self):
        print(f'hhheeaadder: {self.colNames}')
        writer = DictWriter(self.outputFile,fieldnames = self.colNames)
        print(f'includeheader = {self.includeHeader}')

        if self.includeHeader == 'True':
            writer.writeheader()

        for row in self.inputFile:
            rowDict = self.readRow(row)
            writer.writerow(rowDict)

    def readRow(self,row):
        rowDict = {}
        start = 0
        end = 0
        for index in range(len(self.colNames)):
            end += int(self.offsets[index])
            rowDict[self.colNames[index]] = row[start:end]
            start += int(self.offsets[index])
        return rowDict

# if __name__ == "__main__":
#     colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = loadSpec("spec.json")
#     with open("test-input.txt",'r',encoding=fixedWidthEncoding) as inputFile,\
#         open("test-output.csv",'w',encoding=delimitedEncoding, newline='') as outputFile:

    
#         aa = FixedWidthToCsv(inputFile,outputFile,"spec.json")
#         aa.toCsvFile()
    