#!/usr/bin/env python
from distutils.core import setup
from Cython.Distutils import Extension
from Cython.Distutils import build_ext
from glob import glob

import sys
import os
from os.path import splitext

from distutils.sysconfig import get_python_inc
INCLUDES = ['sparsehash/includes']


setup(
    name="sparsehash",
    version="0.2",
    author="Matthew Honnibal",
    author_email="honnibal@gmail.com",
    url="http://github.com/syllog1sm/cython-sparsehash",
    packages=["sparsehash"],
    package_data={"sparsehash": ["*.pxd"]},
    description="""Cython declarations for the Google Sparsehash library.""",
    setup_requires=['Cython >= 0.18'],
    install_requires=['Cython >= 0.18'],
    classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: MIT',
                'Programming Language :: Cython',
                'Topic :: Scientific/Engineering'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension('sparsehash.murmurhash',
            sources=['sparsehash/murmurhash.pyx', 'src/MurmurHash2.cpp', 'src/MurmurHash3.cpp'],
            include_dirs=INCLUDES
        ),
    ],
)
