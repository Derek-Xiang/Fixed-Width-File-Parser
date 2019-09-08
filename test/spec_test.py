import json
import unittest
import os, sys
# sys.path.insert(0, os.path.abspath(".."))

import converter.specLoader as spec
# from ..converter import specLoader


class SpecTest(unittest.TestCase):

    def testFrame(self):
        with open('spec.json','r') as spec_file:
            colNames,offsets,fixedWidthEncoding,includeHeader,delimitedEncoding = spec.loadSpec(spec_file)
            offsetList = ['5','12','3','2','13','7','10','13','20','13']

            self.assertEqual(True,len(colNames)==len(offsets)==10)

            for num in range(len(colNames)):
                self.assertEqual(True, colNames[num] == f'f{num+1}')
                self.assertEqual(True, offsets[num] == offsetList[num])

            self.assertEqual(True, fixedWidthEncoding == "windows-1252")
            self.assertEqual(True, includeHeader == "True")
            self.assertEqual(True, delimitedEncoding == "utf-8")




if __name__ == "__main__":
    unittest.main()


