#!/bin/sh

cd test

echo "========For both tests========:"
python3 testers.py

echo "===For the method loadSpec===:"
python3 -m unittest testers.SpecTest.testSpec
echo "===Test the method readRow===:"
python3 -m unittest testers.SpecTest.testReadRow
echo "===Test the method testCsvGenerator===:"
python3 -m unittest testers.SpecTest.testCsvGenerator
