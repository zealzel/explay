from setuptools import setup, find_packages

setup(
    name="explay",
    packages=["explay"],
    scripts=["bin/exp"],
    version="0.5.0",
    description="make excel jobs playful again",
    author="zealzel",
    author_email="zealzel@gmail.com",
    url="https://github.com/zealzel/explay",
    install_requires=[
        "pandas",
        "openpyxl",
        "regex",
        "fire",
        "XlsxWriter",
        "numpy",
        "xlrd",
        "pyyaml",
        "pretty_html_table",
    ],
)
