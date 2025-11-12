@echo off
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" x64 10.0.19041.0

py -3.12 setup.py build_ext --inplace
del livedm_keys_counter_lib.c
