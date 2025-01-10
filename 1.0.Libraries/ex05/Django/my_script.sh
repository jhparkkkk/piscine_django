#!/bin/bash

echo "Creating Virtual Environment..."

python3 -m venv django_venv
source django_venv/bin/activate

echo "django_venv activated"

pip install --upgrade pip

pip install -r requirement.txt
pip list

