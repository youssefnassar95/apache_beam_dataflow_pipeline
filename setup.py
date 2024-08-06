#!/usr/bin/python
from setuptools import find_packages, setup

setup(
    name="rides_counter",
    version="1.0",
    install_requires=["apache-beam[gcp]==2.33.0"],
    packages=find_packages(),
    include_package_data=True,
    description="Coding Challenge",
)
