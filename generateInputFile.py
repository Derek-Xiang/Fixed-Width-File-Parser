## Program: To generate a valid fixed width file for testing
## version 1.0.0
## Author: Dejun Xiang
## Date: 08/09/2019

import json
from converter.specLoader import loadSpec

def generateTestInput(inputFile, specFile, lines):
    with open(specFile,'r') as spec:
        _, offsets, fixedWidthEncoding, _, _ = loadSpec(specFile)
        with open(inputFile,'w',encoding=fixedWidthEncoding) as file:
            for num in range(lines):
                for offset in offsets:
                    file.write('f'+(int(offset)-1)*offset[0])
                file.write('\n')

if __name__ == "__main__":
    generateTestInput("newTestInput.txt", "spec.json", 3)
