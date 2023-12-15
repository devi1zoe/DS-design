# 使用cx_Freeze库来打包Python应用程序
from cx_Freeze import setup, Executable

files = ['../c_Interface/images/imagesicon.ico','../c_Interface/themes/']

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="../c_Interface/images/imagesicon.ico"
)

setup(
    name = "排课辅助工具",
    version = "1.0",
    description = "排课辅助工具",
    author = "Han Yufan",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)
