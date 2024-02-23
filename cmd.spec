# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cmd.py'],
    pathex=[],
    binaries=[('/home/monkey/micromamba/envs/cmdstanpy/bin/cmdstan', './cmdstan')],
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
