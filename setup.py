#!/usr/bin/python -tt

from distutils.core import setup

setup(
    name='drun',
    version='0.0',
    author='Joshua Carrelli',
    author_email='yew@metareflective.com',
    url='https://bitbucket.org/jcarrelli/drun',
    scripts=['bin/drun'],
    packages=['drun'],
    package_dir={'drun': 'lib'},
    data_files=[('share/drun', ['share/drunrc'])]
)
