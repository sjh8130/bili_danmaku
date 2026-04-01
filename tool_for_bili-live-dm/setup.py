from Cython.Build import cythonize
from setuptools import Extension, setup

a = {
    "define_macros": [
        ("Py_LIMITED_API", 0x030B0000),
    ],
    "py_limited_api": True,
}
setup(
    ext_modules=cythonize(
        [
            Extension(name="livedm_keys_counter_lib", sources=["livedm_keys_counter_lib.py"], **a),
            Extension(name="split_file_base", sources=["split_file_base.py"], **a),
        ],
        # annotate=True,
    ),
)
