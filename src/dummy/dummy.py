#! /usr/bin/env python3
# encoding: utf-8

from dummy import _dummy


def tender() -> int:

    return _dummy.tender()


def foo() -> int:

    d = _dummy._dummy()
    return d.foo(2)
