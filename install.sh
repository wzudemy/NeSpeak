#!/bin/bash
# run with source ./install.sh
sudo apt-get install sox libsndfile1 ffmpeg python3.10-dev
python3.10 -m venv venv_py310
source venv_py310/bin/activate
pip install Cython
pip install nemo_toolkit[asr]