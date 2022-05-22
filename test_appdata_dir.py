from os import path
import shutil
import ghostscript
import win32print
import locale


appdatapath = path.expandvars('%APPDATA%\MyApp')
print(appdatapath)

if shutil.which('gswin64c'):
    print(shutil.which('gswin64c'))



pdf_path = 'C:\\Users\\serra\\GitHub\\huiini_local\\unpdf.pdf'



import os
import subprocess
import sys

# if sys.platform == 'win32':
#     args = '"gswin64c" ' \
#            '-sDEVICE=mswinpr2 ' \
#            '-dBATCH ' \
#            '-dNOPAUSE ' \
#            '-dFitPage ' \
#            '-dQueryUser=3 '
#     ghostscript = args + pdf_path
#     subprocess.call(ghostscript, shell=True)





from tkinter import *

root = Tk()

monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
  
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))

import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)