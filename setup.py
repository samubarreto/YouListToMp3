#python setup.py build
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"build_exe": "YouListToMp3", "packages": ["os", "win32com.client", "win32"], "includes": ["customtkinter", "unidecode", "pytube"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "YouListToMp3",
    version = 1.0,
    description = None,
    options = {"build_exe": build_exe_options},
    executables = [Executable("app.py", base=base)]
)