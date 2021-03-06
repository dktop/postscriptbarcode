#!/usr/bin/env python

"""
setup.py file for postscriptbarcode
"""

from distutils.core import setup, Extension, Command

with open('../../../CHANGES', 'r') as f:
    ver = f.readline().strip().replace("-", "")

class Test(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'example.py'])
        raise SystemExit(errno)

postscriptbarcode_module = Extension(
	'_postscriptbarcode',
	sources=['postscriptbarcode.i'],
	include_dirs = ['../../c'],
	libraries=['postscriptbarcode'],
	library_dirs=['../../c'],
)

setup(name = 'postscriptbarcode',
	version      = ver,
	author       = "Terry Burton",
	author_email = "tez@terryburton.co.uk",
	description  = """Python binding for Barcode Writer in Pure PostScript""",
	url          = "http://bwipp.terryburton.co.uk",
	ext_modules  = [postscriptbarcode_module],
	py_modules   = ["postscriptbarcode"],
	cmdclass     = {'test': Test},
)

