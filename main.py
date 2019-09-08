import sys,logging
from converter.specLoader import loadSpec
from converter.converterToCsv import FixedWidthToCsv

logging.basicConfig(filename='FixedWidthToCsv_Error.log', level=logging.ERROR,
					format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Please input your command as : python main.py <inputFile> <outputFile.csv> <specFile.json>")

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    specFile = sys.argv[3]

    try:
        colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = loadSpec(specFile)
        with open(inputFile,'r',encoding=fixedWidthEncoding) as inputFile,\
            open(outputFile,'w',encoding=delimitedEncoding, newline='') as outputFile:

            aa = FixedWidthToCsv(inputFile,outputFile,specFile)
            aa.toCsvFile()
    except:
        logging.ERROR("Check what is going on")




# python -m unittest spec_test.SpecTest.testSpec
# python -m unittest spec_test.SpecTest.testReadRow




