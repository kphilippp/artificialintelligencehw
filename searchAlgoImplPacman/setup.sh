#!/usr/bin/env bash

apt-get install -y python3.8 python3.8-dev python3.8-distutils python3.8-venv
python3 --version

pip3 install -r /autograder/source/requirements.txt
