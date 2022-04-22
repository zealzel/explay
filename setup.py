from setuptools import setup, find_packages

setup(
    name="explay",
    packages=["explay"],
    version="0.6.0",
    description="make excel jobs playful again",
    author="zealzel",
    author_email="zealzel@gmail.com",
    url="https://github.com/zealzel/explay",
    install_requires=[
        "pandas",
        "openpyxl",
        "regex",
        "XlsxWriter",
        "numpy",
        "xlrd",
        "pyyaml",
        "pretty_html_table",
    ],
    entry_points={
        "console_scripts": [
            "exp = explay.exp:main",
        ],
    },
)
