# mylib

Library to test sphinx docs

## Installation

    mamba install -c conda-forge sphinx m2r2 sphinx_rtd_theme sphinx_mdinclude
## Quickstart sphinx

```
sphinx-quickstart docs
> Separate source and build directories (y/n) [n]: y


docs
├── Makefile
├── build
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst

sphinx-apidoc -e --ext-autodoc -f -o source/api/package ../mylib
sphinx-apidoc -e --ext-autodoc -f -o source/api/scripts ../scripts
sphinx-build -M html source build

or 

make html


# GitHub pages

https://rosatrancoso.github.io/mylib/

```
