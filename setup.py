import sys
from cx_Freeze import setup, Executable

setup(
    name = "Web-Browser",
    version = "1.0.0",
    description = "Web-Browser :)",
    executables = [Executable("main.py", base = "Win32GUI", icon="icon.ico")])