#! /usr/bin/env python3
# encoding: utf-8

from dummy import _dummy


def tender():

    return _dummy.tender()


def foo():

    d = _dummy._dummy()
    return d.foo(2)
