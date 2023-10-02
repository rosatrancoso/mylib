#!/usr/bin/env python
# from distutils.core import setup

# https://packaging.python.org/tutorials/packaging-projects/
import setuptools

setuptools.setup(
    name="mylib",
    version="0.1",
    description="Test setup development",
    author="R2D2",
    author_email="r2d2@starwars.com",
    url="https://www.erabomera.com",
    packages=setuptools.find_packages(),
    scripts=["scripts/myscript.sh"],
)
