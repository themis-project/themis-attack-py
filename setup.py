# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
import os


about = {}
about_filename = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'themis', 'attack', '__about__.py')
with io.open(about_filename, 'rb') as fp:
    exec(fp.read(), about)


setup(
    name='themis.attack',
    version=about['__version__'],
    description='Themis Finals attack helper library',
    author='Alexander Pyatkin',
    author_email='asp@thexyz.net',
    url='https://github.com/aspyatkin/themis-attack-py',
    license='MIT',
    packages=find_packages('.'),
    install_requires=[
        'setuptools',
        'enum34>=1.0',
        'requests>=2.7'
    ],
    namespace_packages=['themis'],
    entry_points={
        'console_scripts': [
            'themis-attack = themis.attack.main:run',
        ]
    }
)
