#!/usr/bin/env python
import Cython.Distutils
from distutils.extension import Extension
import distutils.core

import sys
import os
from os.path import join as pjoin


def clean(ext):
    for pyx in ext.sources:
        if pyx.endswith('.pyx'):
            c = pyx[:-4] + '.c'
            cpp = pyx[:-4] + '.cpp'
            so = pyx[:-4] + '.so'
            if os.path.exists(so):
                os.unlink(so)
            if os.path.exists(c):
                os.unlink(c)
            elif os.path.exists(cpp):
                os.unlink(cpp)


pwd = os.path.dirname(__file__)

includes = [os.path.join(pwd, 'sparsehash')]
libs = [os.path.join(pwd, 'sparsehash')]

exts = [
    Extension('ext.murmurhash', ["sparsehash/murmurhash.pyx", "sparsehash/MurmurHash2.cpp",
              "sparsehash/MurmurHash3.cpp"], language="c++", include_dirs=includes),
    Extension('ext.sparsehash', ["sparsehash/sparsehash.pyx"], language="c++",
              include_dirs=includes),
]


if sys.argv[1] == 'clean':
    print >> sys.stderr, "cleaning .c, .c++ and .so files matching sources"
    map(clean, exts)

distutils.core.setup(
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    description='Cython wrapper for sparsehash and MurmurHash',
    keywords='sparsehash densehash murmur murmurhash cython',
    license='MIT',
    name='sparsehash',
    packages=['sparsehash'],
    author='Matthew Honnibal',
    author_email='honnibal@gmail.com',
    version='0.11',
    url='http://github.com/syllog1sm/cython-sparsehash',
    cmdclass={'build_ext': Cython.Distutils.build_ext},
    ext_modules=exts,
)



