#!/bin/bash

python3 -m venv venv
virtualenv venv
source venv/bin/activate
python3 -m pip install -r req.txt