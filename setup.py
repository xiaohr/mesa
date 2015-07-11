#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open

requires = [
    'tornado',
    'numpy',
    'pandas',
]

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='Mesa',
    version='0.6.5',
    description="Mesa: Agent-based modeling in Python 3+",
    long_description=readme,
    author='Project Mesa Team',
    author_email='projectmesa@googlegroups.com',
    url='https://github.com/projectmesa/mesa',
    packages=find_packages(),
    package_data={'mesa': ['visualization/templates/*']},
    include_package_data=True,
    install_requires=requires,
    keywords='agent based modeling model ABM simulation multi-agent',
    license='Apache 2.0',
    zip_safe=False,
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
    ],
)
