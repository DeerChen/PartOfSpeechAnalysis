# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['entry.py'],
             pathex=['C:\\Users\\千北\\Desktop\\新建文件夹'],
             binaries=[],
             datas=[],
             hiddenimports=['openpyxl', 'pysimplegui', 'textblob', 'pandas'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='词性词频分析',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='funny.ico')