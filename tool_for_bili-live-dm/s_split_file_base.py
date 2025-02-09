from Cython.Build import cythonize
from setuptools import setup

setup(ext_modules=cythonize(["split_file_base.py"], annotate=False))
