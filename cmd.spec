# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['cmd.py'],
    pathex=['C:\Program Files (x86)\Intel\oneAPI\mkl\2022.1.0\redist\intel64'],
    binaries=[],
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
