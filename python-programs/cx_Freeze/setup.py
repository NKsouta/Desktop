# coding: utf-8
# Setup file for cx_Freeze

import sys
import os
os.environ['TCL_LIBRARY'] = "C:\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Anaconda3\\tcl\\tk8.6"
from cx_Freeze import setup, Executable

# -------
# Setup
# -------
packages = ["chainer"]
includes = ["scipy","numpy","chainer"]
excludes = []
binpaths = []
binincludes = ['C:/Program Files (x86)/IntelSWTools']
init_script = "ConsoleSetLibPath"

# exe にしたい python ファイルを指定
Target = "./target.py"

base = None

# GUI=有効, CUI=無効 にする
# if sys.platform == 'win32' : base = 'Win32GUI'

# if sys.platform == 'win32' : base = 'Win32GUI'

exe = Executable(script = Target,
                 base = base)
#training_approximate
#train_cifar
# セットアップ
setup(name = 'test',
      version = '0.1',
      description = 'converter',
      options = {"build_exe": {"includes":includes, 
                               "excludes":excludes, "packages":packages, 
                               'bin_path_includes':binpaths, 'bin_includes':binincludes, 
                               }},
      executables = [exe])
