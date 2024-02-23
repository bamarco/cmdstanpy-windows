# -*- mode: python ; coding: utf-8 -*-

import os
import json
import subprocess

def mmamba_path():
    shellout = subprocess.run(['micromamba', '--json', 'info'], stdout=subprocess.PIPE).stdout
    outstr = shellout.decode("utf-8")
    info = json.loads(outstr)
    path = info['env location']
    return path

def mmamba_lib_bin_path():
    return os.path.join(mmamba_path(), 'Library', 'bin')

def mmamba_bin_path():
    return os.path.join(mmamba_path(), 'bin')

a = Analysis(
    ['cmd.py'],
    pathex=[],
    binaries=[(mmamba_lib_bin_path(), '.'), (mmamba_bin_path(), '.'), (os.path.join(os.environ['CMDSTAN']), './cmdstan')],
    datas=[('bernoulli.stan', '.'), ('bernoulli.data.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['env_patch.py'],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cmd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
