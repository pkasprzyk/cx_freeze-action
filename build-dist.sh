#!/bin/bash

rm -fr dist/
cxfreeze -c sample.py --target-dir $1
cp -r resources dist/
