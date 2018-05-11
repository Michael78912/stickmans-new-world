
# this a try. Pretty sure this will assume your Python install is part of your PATH.
import sys
import os
from cx_Freeze import setup, Executable
import cx_Freeze
import tkinter
import os.path
import scipy

base = None

if sys.platform == 'win32':
    base = "Win32GUI"


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

#os.environ['TCL_LIBRARY'] = r'C:\Users\matthew\Downloads\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\Users\matthew\Downloads\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\tcl\tk8.6'

executables = [cx_Freeze.Executable("terrain_viewer.py", base=base), icon='icon.ico']
addtional_mods = ['numpy.core._methods', 'numpy.lib.format']

packages = ["idna", "numpy",]
options = {
    'build_exe': {

        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            os.path.dirname(scipy.__file__),

         ],
        'includes': addtional_mods,
        'packages':packages,
    },

}

cx_Freeze.setup(
    name = "vefr",
    options = options,
    version = "0.01",
    description = 'testing',
    executables = executables
)