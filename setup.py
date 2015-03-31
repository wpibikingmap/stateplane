#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/someuser/somepackage

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup, find_packages

setup(
    name='stateplane',
    version='0.1.0',
    description='Convert between state plane projections and long/lat',
    long_description=open('readme.rst').read(),
    keywords='gis usa projection',
    author='Neil Freeman',
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/stateplane',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fiona>=1.4.8,<1.6',
        'pyproj>=1.9.4,<2',
        'shapely>=1.5.1,<1.6',
    ],
    test_suite='tests',
    tests_require=[
        'coverage',
        'tox',
    ],
    entry_points={
        'console_scripts': [
            'stateplane=stateplane.cli:main',
        ],
    },
    zip_safe=False,
)