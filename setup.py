# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name='tasklegion',
    version=version,
    description='Adding collaborative functionality to TaskWarrior',
    author='Nikolai Nowaczyk',
    author_email='mail@nikno.de',
    license='GNU GPLv2',
    url='https://github.com/niknow/TaskLegion',
    packages=find_packages(),
    install_requires=['tasklib==0.8.0']
)