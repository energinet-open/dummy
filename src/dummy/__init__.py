#! /usr/bin/env python3
# encoding: utf-8

from __future__ import absolute_import
from pkg_resources import get_distribution

# Functions that are available after importing the module
from dummy.dummy import foo
from dummy.dummy import tender

# Setup what to run if executed as an application
from dummy.__main__ import run

# This automatically extract the version using setuptool-scm
# https://pypi.org/project/setuptools-scm/
__version__ = get_distribution(__name__).version
