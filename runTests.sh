#!/bin/sh

cd test

echo "========For both tests========:"
python testers.py

echo "===For the method loadSpec===:"
python -m unittest testers.SpecTest.testSpec
echo "===Test the method readRow===:"
python -m unittest testers.SpecTest.testReadRow