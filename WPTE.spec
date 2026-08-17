a = Analysis(
    ['mainwindow.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'unittest', 'email', 'http',
        'pydoc', 'doctest', 'difflib',
        'pickle', 'calendar', 'pprint',
    ],
    noarchive=False,
    optimize=2,  # strips docstrings + assert statements
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,   # moved here for onefile
    a.datas,      # moved here for onefile
    [],
    name='WPTE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,   # strips debug symbols
    upx=True,
    upx_exclude=[],
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons\\icon.ico',
)
