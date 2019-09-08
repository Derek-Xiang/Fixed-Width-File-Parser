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
        rowDict[colNames[index]] = row[start:end]
        start += int(offsets[index])
    return rowDict


        
