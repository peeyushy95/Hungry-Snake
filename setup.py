from cx_Freeze import setup, Executable
import sys

productName = "ProductName"
if 'bdist_msi' in sys.argv:
    sys.argv += ['--initial-target-dir', 'C:\InstallDir\\' + productName]
    sys.argv += ['--install-script']

exe = Executable(
      script="hungrySnake.py",
      base="Win32GUI",
      targetName="Product.exe"
     )
setup(
      name="Product.exe",
      version="1.0",
      author="Me",
      description="Copyright 2012",
      executables=[exe])
	  
