from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension(name="wrap",
				library_dirs=['/home/zywang/gsl/lib'],
                libraries=['m', 'gsl', 'gslcblas'], 
                sources=["sigma.c", "vars.c","wrap.pyx"])

setup(ext_modules=cythonize(ext))