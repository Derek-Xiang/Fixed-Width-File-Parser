# Parse fixed width file
**Version 1.0.1 **<br>
Modified with the guidance provided<br>
+++ add test: "testCsvGenerator"<br>
+++ modify generateInputFile.py to generate input file by spec.json (no hard coding)<br>
+++ modify runTest.sh file
<br>
Command to run to check: ./runTests.sh

**Version 1.0.0 **

This program is to convert a fixed width file to a csv file with a spec file
### Dependency:
None <br>
Pure Python3 

### How to use the file Converter:
python3 main.py (inputFile) (outputFile.csv) (specFile.json)

### Example:
python3 main.py testInput.txt testOutput.csv spec.json

### How to run unit tests:
chmod +x runTests.sh <br>
./runTests.sh
