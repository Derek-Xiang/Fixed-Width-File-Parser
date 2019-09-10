#!/bin/sh

cd test

echo "========For all tests========:"
python3 testers.py
echo "===For the method loadSpec===:"
python3 -m unittest testers.SpecTest.testSpec
echo "===Test the method readRow===:"
python3 -m unittest testers.SpecTest.testReadRow

echo "===Test the method testCsvGenerator===:"
echo 1.. generate file "generateInputFile.txt" by spec file
cd ..
python3 generateInputFile.py
echo 2.. convert it to csv file ..
python3 main.py newTestInput.txt newTestOutput.csv spec.json
echo 3.. csv file "newTestOutput.csv" is generated ..
echo 4.. test the testCsvGenerator method ..
cd test
python3 -m unittest testers.SpecTest.testCsvGenerator
