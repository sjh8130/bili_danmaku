@echo off
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" x64 10.0.19041.0

py -3.10 s_split_file_base.py build_ext --inplace
del split_file_base.c
py -3.11 s_split_file_base.py build_ext --inplace
del split_file_base.c
py -3.12 s_split_file_base.py build_ext --inplace
del split_file_base.c
py -3.13 s_split_file_base.py build_ext --inplace
del split_file_base.c
py -3.13t s_split_file_base.py build_ext --inplace
del split_file_base.c
