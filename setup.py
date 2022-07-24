## setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

print(find_packages())

setup(
    name = 'openKMA',
    version = '0.1.6',    
    description = 'Not yet description',
    url = 'https://github.com/taeyoon32/openKMA',
    author = 'Taeyoon Eom',
    author_email = 'eom.taeyoon.kor@gmail.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = ['requests',
                        'xmltodict',
                        'pandas',
                        'numpy'
                        ]
)