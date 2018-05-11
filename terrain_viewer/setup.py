from cx_Freeze import Executable, setup
import sys
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

opt =  {
    "packages": ['pygame','_cffi_backend', 'cryptography', 'tkinter', 'idna', '_tkinter'],
    'includes': ['_tkinter', 'numpy.core._methods', 'numpy.lib.format'],
    "excludes": ['scipy', 'test'],
    'include_files': [
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        'data',
        'terrains',
        'icon.ico',
        'email_icon.ico'
        ],
    "include_msvcr": True,
    }

base = 'Win32GUI' if sys.platform == 'win32' else None

setup(
    name='SMR Terrain Viewer',
    version='0.1',
    description='displays smr-terrain files',
    options = {'build_exe': opt},
    executables=[Executable('terrain_viewer.py', icon='icon.ico', base=base)]
) 
