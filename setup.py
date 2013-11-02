#!/usr/bin/env python

"""Setup script for packaging openpyxl.

Requires setuptools.

To build the setuptools egg use
    python setup.py bdist_egg
and either upload it to the PyPI with:
    python setup.py upload
or upload to your own server and register the release with PyPI:
    python setup.py register

A source distribution (.zip) can be built with
    python setup.py sdist --format=zip

That uses the manifest.in file for data files rather than searching for
them here.

"""

import sys
import warnings

if sys.version_info < (2, 6):
    raise Exception("Python >= 2.6 is required.")

from setuptools import setup, Extension, find_packages
import openpyxl  # to fetch __version__ etc

setup(name = 'openpyxl',
    packages = find_packages(),
    # metadata
    version = openpyxl.__version__,
    description = "A Python library to read/write Excel 2007 xlsx/xlsm files",
    long_description = 'openpyxl is a pure python reader and writer of '
        'Excel OpenXML files.  It is ported from the PHPExcel project',
    author = openpyxl.__author__,
    author_email = openpyxl.__author_email__,
    url = openpyxl.__url__,
    license = openpyxl.__license__,
    download_url = openpyxl.__downloadUrl__,
    test_suite = 'nose.collector',
    tests_require = ['nose', 'lxml'],
    classifiers = ['Development Status :: 4 - Beta',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'],
    )
