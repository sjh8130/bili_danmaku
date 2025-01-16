from Cython.Build import cythonize
from setuptools import setup

setup(ext_modules=cythonize(["livedm_keys_counter_lib.py"], annotate=False))
