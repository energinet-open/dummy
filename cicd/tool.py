#! /usr/bin/env python3
# encoding: utf-8

import argparse
import glob
import os
import shutil
import subprocess

import base_tool


def _setup(**kwargs):
    """
    Setup the environment installing all dependencies in the requirement files.
    """

    subprocess.run(
        "pip install -r cicd/requirements.txt ", shell=True, check=True
    )

    subprocess.run(
        "pip install -r src/requirements.txt ", shell=True, check=True
    )

    subprocess.run(
        "pip install -r test/requirements.txt", shell=True, check=True
    )

    subprocess.run("pip install -e .", shell=True, check=True)


def _build(**kwargs):
    raise Exception("build step not implemented")


def _test(**kwargs):
    """
    Run the tests
    """

    try:

        if kwargs['requirements']:
            print("Checking installed dependencies.")
            base_tool.check_requirements()

        if kwargs['pep8']:
            print("Checking pep8 conformance.")
            subprocess.run(
                'flake8 --per-file-ignores="__init__.py:F401"',
                shell=True,
                check=True,
            )

        if kwargs['license']:
            print("Checking license of used dependencies.")
            subprocess.run(
                'liccheck -s cicd/licenses.ini \
                    -r src/requirements.txt \
                    -r test/requirements.txt',
                shell=True,
                check=True,
            )

        if kwargs['static']:
            print("Running static analysis check.")
            subprocess.run(
                'mypy src test/*/ --config-file cicd/mypy.ini',
                shell=True,
                check=True
            )

        if kwargs['test_files']:
            print("Checking for test files for all source files.")
            base_tool.check_test_files(
                "src/template_advanced_analytics_service/", "test/src/")

        if kwargs['unittests']:
            print("Running unittests.")
            subprocess.run(
                'pytest test/src/ \
                    --cov-fail-under=100 \
                    --durations=5 \
                    -vv',
                shell=True,
                check=True
            )

    except subprocess.CalledProcessError as e:
        exit(e.returncode)


def _update(**kwargs):

    base_tool.update_requirements()


def _clean(**kwargs):

    for path in glob.glob('**/__pycache__', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/*egg-info', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/.coverage', recursive=True):
        os.remove(path)

    for path in glob.glob('**/.*cache', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/model.pickle', recursive=True):
        os.remove(path)


def _release(**kwargs):
    
    raise Exception("relase step not implemented")


def cli():

    parser = argparse.ArgumentParser(description='Tool')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_setup = subparsers.add_parser('setup', help='install dependencies.')
    parser_setup.set_defaults(func=_setup)

    parser_test = subparsers.add_parser('test', help='run tests')
    parser_test.set_defaults(func=_test)

    parser_test.add_argument(
        '--no-requirements',
        dest='requirements',
        action='store_false',
        help='diable check that correct requirements are installed.'
    )

    parser_test.add_argument(
        '--no-pep8',
        dest='pep8',
        action='store_false',
        help='disable pep 8 check.'
    )

    parser_test.add_argument(
        '--no-static',
        dest='static',
        action='store_false',
        help='disable static checks of source.'
    )

    parser_test.add_argument(
        '--no-license',
        dest='license',
        action='store_false', help='disable check of licenses in requirements.'
    )

    parser_test.add_argument(
        '--no-test_files',
        dest='test_files',
        action='store_false',
        help='disable test that all py files have a corresponding test file.'
    )

    parser_test.add_argument(
        '--no-unittests',
        dest='unittests',
        action='store_false',
        help='disable unittests.'
    )

    parser_clean = subparsers.add_parser(
        'clean',
        help='remove various temporary files.'
        )
    parser_clean.set_defaults(func=_clean)

    parser_update = subparsers.add_parser(
        'update',
        help='update dependencies to newest versions.'
    )
    parser_update.set_defaults(func=_update)

    parser_release = subparsers.add_parser(
        'release',
        help='release the module or cli.'
    )
    parser_release.set_defaults(func=_release)

    return parser


if __name__ == '__main__':

    parser = cli()
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(**vars(args))
    else:
        parser.print_help()
