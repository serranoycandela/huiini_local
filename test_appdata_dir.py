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
# args = [
#         "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
#         "-q",
#         "-dNumCopies#1",
#         "-sDEVICE#mswinpr2",
#         f'-sOutputFile#"%printer%{win32print.GetDefaultPrinter()}"',
#         f'"{pdf_path}"'
#     ]

# encoding = locale.getpreferredencoding()
# args = [a.encode(encoding) for a in args]
# print(args)

# ghostscript.Ghostscript(*args)


import os
import subprocess
import sys

if sys.platform == 'win32':
    args = '"C:\\\\Program Files\\\\gs\\\\gs9.56.1\\\\bin\\\\gswin64c" ' \
           '-sDEVICE=mswinpr2 ' \
           '-dBATCH ' \
           '-dNOPAUSE ' \
           '-dFitPage ' \
           '-sOutputFile="%printer%{win32print.GetDefaultPrinter()}" '
    ghostscript = args + pdf_path
    subprocess.call(ghostscript, shell=True)




# GHOSTSCRIPT_PATH = "C:\path\to\GHOSTSCRIPT\bin\gswin32.exe"
# GSPRINT_PATH = "C:\path\to\GSPRINT\gsprint.exe"

# # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
# currentprinter = win32print.GetDefaultPrinter()

# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "PDFFile.pdf"', '.', 0)