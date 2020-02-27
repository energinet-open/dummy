python_module_template
======================

A python project template. You can use this as a starting point for a Python module or cli.

Getting Started
---------------

::

    git clone git@github.com:energinet-open/dummy.git


To install test dependencies locally and run basic tests

::

    python3 -m venv test-env
    source test-env/bin/activate
    cd dummy
    python tool setup

Run all tests as executed when commits are pushed.

::

    python tool test


Overview
--------

Read this


https://docs.pytest.org/en/latest/goodpractices.html



setuptools
..........

edit /setup.py


Setuptools https://setuptools.readthedocs.io/en/latest/

https://pypi.org/classifiers/


Versioning:

- automatically handled using setuptools_scm - just make a release in git



unittests
.........



pytest
......



Type hinting
............

https://www.python.org/dev/peps/pep-0484/


http://mypy-lang.org/

https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html



If you are using Visual Studio Code you can also consider

https://github.com/microsoft/pyright

Implemented in typescript




For the future
--------------

Consider

PEP518 pyproject.toml
https://snarky.ca/clarifying-pep-518/
https://hackersandslackers.com/python-poetry/

tox
to be considered
