from distutils.core import setup, Extension
from Cython.Build import cythonize
import platform, glob, sys

extensions=[Extension("foo.foo",sources=["foo/foo.pyx"]),
            Extension("foo.foo2.foo2",sources=["foo/foo2/foo2.pyx"]),
]

setup(name="foo",
      ext_modules=cythonize(extensions))
