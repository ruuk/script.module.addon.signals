#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, unicode_literals
from setuptools import setup, find_packages
import os
from xml.dom.minidom import parse

project_dir = os.path.dirname(os.path.abspath(__file__))
metadata = parse(os.path.join(project_dir, 'addon.xml'))
addon_version = metadata.firstChild.getAttribute('version')
addon_id = metadata.firstChild.getAttribute('id')

setup(
    name='AddonSignals',
    version=addon_version,
    url='https://github.com/ruuk/script.module.addon.signals',
    author='Rick Phillips',
    description='Kodi Addon Signals',
    long_description=open(os.path.join(project_dir, 'README.md')).read(),
    keywords='Kodi, plugin, addon, signals',
    license='LGPL-2.1-only',
    py_modules=['AddonSignals'],
    package_dir={'': 'lib'},
    zip_safe=False,
    platforms=['all'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
)
