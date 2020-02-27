#! /usr/bin/env python3
# encoding: utf-8

import dummy


def test_version():

    assert(dummy.__version__)


def test_foo():

    assert dummy.foo() == 0


def test_tender():

    assert dummy.tender() == 42
