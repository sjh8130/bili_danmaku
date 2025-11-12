from Cython.Build import cythonize
from setuptools import Extension, setup

# setup(ext_modules=cythonize(["split_file_base.py"], annotate=False))
setup(ext_modules=cythonize([Extension(name="split_file_base", sources=["split_file_base.py"], define_macros=[("Py_LIMITED_API", 0x030B0000)], py_limited_api=True)]))
