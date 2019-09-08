## Program: Two functions:
##          1. Load spec file
##          2. read lines for input file.
## version 1.0.0
## Author: Dejun Xiang
## Date: 08/09/2019

import json

def loadSpec(spec_file):
    with open(spec_file,'r') as file:
        spec = json.load(file)
        colNames=spec["ColumnNames"]
        offsets=spec["Offsets"]
        fixedWidthENcoding = spec["FixedWidthEncoding"]
        includeHeader = spec['IncludeHeader']
        delimitedEncoding = spec["DelimitedEncoding"]
        return colNames, offsets, fixedWidthENcoding, includeHeader, delimitedEncoding

def readRow(row, colNames, offsets):
    rowDict = {}
    start = 0
    end = 0
    for index in range(len(colNames)):
        end += int(offsets[index])
        # fill the rowDict its header corresponding with its content
        rowDict[colNames[index]] = row[start:end]
        start += int(offsets[index])
    return rowDict


        
