import unittest
import sys,os,io
sys.path.insert(0, os.path.abspath(".."))
import converter.specLoader as spec

class SpecTest(unittest.TestCase):

    def testSpec(self):
        # with open('spec.json','r') as spec_file:
        colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = spec.loadSpec('..\\spec.json')
        offsetList = ['5','12','3','2','13','7','10','13','20','13']

        self.assertEqual(True,len(colNames)==len(offsets)==10)

        for num in range(len(colNames)):
            self.assertEqual(f'f{num+1}', colNames[num])
            self.assertEqual(offsetList[num], offsets[num])

        self.assertEqual("windows-1252", fixedWidthEncoding)
        self.assertEqual('True', includeHeader)
        self.assertEqual('utf-8', delimitedEncoding)

    def testReadRow(self):
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
        inputText = "f1111f22222222222f33f4f555555555555f666666f777777777f888888888888f9999999999999999999f100000000000"
        colNames = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
        offsets = ['5','12','3','2','13','7','10','13','20','13']
        rowDict = spec.readRow(inputText, colNames,offsets)
        self.assertEqual(row, rowDict)

if __name__ == "__main__":
    unittest.main()


