# -*- mode: python ; coding: utf-8 -*-

import os
import json
import subprocess

def env_path():
    shellout = subprocess.run(['micromamba', '--json', 'info'], stdout=subprocess.PIPE).stdout
    outstr = shellout.decode("utf-8")
    info = json.loads(outstr)
    path = info['env location']
    return path

def bin_path():
    return os.path.join(env_path(), 'Library', 'bin')

# need C:\/Users/runneradmin/micromamba/envs/cmdstanpy/Library/bin/mkl_intel_thread.2.dll in windows

print(bin_path())
