#  from distutils.core import setup
from setuptools import setup

setup(
    name = 'explay_testr',
    packages = ['explay'],
    scripts = ['bin/exp'],
    version = '0.3.3',
    description = 'make excel jobs playful again',
    author = 'zealzel',
    author_email = 'zealzel@gmail.com',
    url = 'https://github.com/zealzel/explay',
    download_url = 'https://github.com/zealzel/explay/tarball/v0.3.3',
    #  keywords = ['pandas', 'openpyxl', 'fire'],
    #  classifiers = [],
    install_requires=[
        'pandas',
        'openpyxl',
        'regex',
        'fire',
        'XlsxWriter',
        'numpy',
        'xlrd',
        'pyyaml',
    ]
)
