#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='demo-cmdpystan',
      version='0.1',
      packages=find_packages(),
      scripts=["cmd.py"],
      )
