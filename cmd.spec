# -*- mode: python ; coding: utf-8 -*-

import os
import json

def env_path():
    shellout = os.popen('micromamba info --json')
    info = json.loads(shellout.read())
    path = info['env location']
    return path

def bin_path():
    os.path.join(env_path(), 'Library', 'bin')

# need C:\/Users/runneradmin/micromamba/envs/cmdstanpy/Library/bin/mkl_intel_thread.2.dll in windows

a = Analysis(
    ['cmd.py'],
    pathex=[bin_path()],
    binaries=['mkl_intel_thread.2.dll'],
    datas=[('bernoulli.stan', '.'), ('bernoulli.data.json', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
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
