from csv import DictWriter
from converter.specLoader import loadSpec,readRow

class FixedWidthToCsv():

    def __init__(self,inputFile,outputFile,specFile):

        self.inputFile = inputFile
        self.outputFile = outputFile
        self.specFile = specFile
        self.colNames,self.offsets,self.fixedWidthEncoding,self.includeHeader,self.delimitedEncoding = loadSpec(specFile)

    def toCsvFile(self):
        writer = DictWriter(self.outputFile,fieldnames = self.colNames)
        if self.includeHeader == 'True':
            writer.writeheader()

        for row in self.inputFile:
            rowDict = readRow(row, self.colNames, self.offsets)
            writer.writerow(rowDict)

# if __name__ == "__main__":
#     colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = loadSpec("spec.json")
#     with open("..\\testInput.txt",'r',encoding=fixedWidthEncoding) as inputFile,\
#         open("test-output.csv",'w',encoding=delimitedEncoding, newline='') as outputFile:
#
#         aa = FixedWidthToCsv(inputFile,outputFile,"spec.json")
#         aa.toCsvFile()
    