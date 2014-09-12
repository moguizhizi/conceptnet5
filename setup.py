#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

packages = find_packages()
version_str = '5.3b1'

if sys.version_info.major == 2:
    nltk_version = 'nltk'
else:
    nltk_version = 'nltk >= 3.0b'

setup(
    name = 'ConceptNet',
    version = version_str,
    description = 'A semantic network of general knowledge',
    author = "Rob Speer",
    author_email = 'conceptnet@media.mit.edu',
    packages=packages,
    package_data={'conceptnet5': ['support_data/*']},
    install_requires=[nltk_version, 'assoc-space', 'xmltodict', 'pyyaml', 'flask', 'flask-cors', 'grako > 3', 'ftfy', 'msgpack-python'],
    license = 'GPLv3'
)

