#! /usr/bin/env python3
# encoding: utf-8

import sys
import argparse


def cli():
    '''
    Dummy command line interface using argparse
    https://docs.python.org/3/library/argparse.html
    '''

    parser = argparse.ArgumentParser(description='''
        Dummy command line interface
        ''')

    args = sys.argv[1:]

    parser.add_argument('--command', type=str, required=True,
                        help='Prints the argument.')

    args = parser.parse_args(args)

    return args


def run():

    if sys.version_info < (3, 5):
        raise RuntimeError("Requires Python 3.5+")


if __name__ == "__main__":

    run()
