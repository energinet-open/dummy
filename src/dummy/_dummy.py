#! /usr/bin/env python3
# encoding: utf-8


class _dummy:

    def __init__(self):

        self._number = 0

    def foo(self, parameter) -> int:
        return self._number

    def _bar(self, parameter: str) -> str:
        return parameter


def tender():
    return 42
