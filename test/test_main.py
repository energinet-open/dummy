#! /usr/bin/env python3
# encoding: utf-8

import dummy


def test_main():

    assert(dummy.__main__)

    dummy.__main__.run_command(command = 'foo')

    dummy.__main__.run_command(command = 'tender')