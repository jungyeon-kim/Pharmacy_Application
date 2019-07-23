block_cipher = None


a = Analysis(['main.py'],
         pathex=['C:\\Users\\zoemf\\Desktop\\Git\\Pharmacy_Application\\project'],
         binaries=[],
         datas=[
         ("C:\\Users\\zoemf\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\branca\\*.json","branca"),
         ("C:\\Users\\zoemf\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\branca\\templates","templates"),
         ("C:\\Users\\zoemf\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\folium\\templates","templates"),
         ],
         hiddenimports=[],
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
      name='main',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      runtime_tmpdir=None,
      console=True )