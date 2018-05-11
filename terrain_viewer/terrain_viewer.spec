# -*- mode: python -*-

block_cipher = None


a = Analysis(['terrain_viewer.py'],
             pathex=["C:\\Users\\Michael\\OneDrive\\stickman's_new_world\\terrain_viewer"],
             binaries=[],
             datas=[('icon.ico', ''), ('email_icon.ico', '')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='terrain_viewer',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='terrain_viewer',
	 icon='icon.ico')
