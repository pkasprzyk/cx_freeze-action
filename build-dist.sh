#!/bin/bash

rm -fr dist/
cxfreeze -c sample.py --target-dir dist
cp -r resources dist/
