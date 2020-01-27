#! /usr/bin/env python3
# encoding: utf-8

import subprocess

subprocess.run('flake8 --per-file-ignores="__init__.py:F401"', shell=True)
subprocess.run('pytest --mypy src test', shell=True)
subprocess.run('pytest --cov=dummy test/ --cov-fail-under=70 '
               '--durations=5 -vv', shell=True)
