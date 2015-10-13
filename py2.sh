#!/bin/sh

alias python=python2
sh clean.sh
python setup.py build_ext -i
python test.py
