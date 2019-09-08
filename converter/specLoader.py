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


        
