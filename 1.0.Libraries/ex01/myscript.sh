#!/bin/bash

pip --version

pip install git+https://github.com/jaraco/path.git --target=./local_lib --upgrade --log install.log

python3 my_program.py