#!/usr/bin/env python3
import os

# add flag to pyinstaller:
# --runtime-hook env_patch.py

os.environ['CMDSTAN'] = os.path.abspath(os.path.join(sys._MEIPASS, 'cmdstan'))
