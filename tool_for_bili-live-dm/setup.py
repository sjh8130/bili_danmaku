from Cython.Build import cythonize
from setuptools import Extension, setup

# setup(ext_modules=cythonize(["livedm_keys_counter_lib.py"], annotate=False))
setup(ext_modules=cythonize([Extension(name="livedm_keys_counter_lib", sources=["livedm_keys_counter_lib.py"], define_macros=[("Py_LIMITED_API", 0x030B0000)], py_limited_api=True)]))
