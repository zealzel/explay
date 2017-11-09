#  from distutils.core import setup
from setuptools import setup

setup(
    name = 'explay_test1',
    packages = ['core'],
    scripts = ['bin/exp'],
    version = '0.1.0',
    description = 'make excel jobs playful again',
    author = 'zealzel',
    author_email = 'zealzel@gmail.com',
    url = 'https://github.com/zealzel/explay',
    download_url = 'https://github.com/zealzel/explay/tarball/v0.1',
    #  keywords = ['pandas', 'openpyxl', 'fire'],
    #  classifiers = [],
    install_requires=[
        'pandas',
        'openpyxl',
        'regex',
        'fire',
        'XlsxWriter',
        'numpy',
        'xlrd'
    ]
)
