#! /usr/bin/env python3
# encoding: utf-8

import argparse
import glob
import os
import shutil
import subprocess


def _check_requirements():
    """
    Check that all requirements in the environment corresponds to what is
    specified in the requirement files.
    """

    requirements = glob.glob('*/*requirements.txt', recursive=True)

    for r in requirements:
        subprocess.run(f"requirementz --file {r}", shell=True, check=True)


def _check_test_files(src_path, test_path):
    """
    check that for each file.py in the src_path there is a corresponding
    test_file.py in the test_path.
    """

    test_paths = glob.glob(f'{test_path}/*.py')
    test_sub_paths = []
    for tp in test_paths:
        test_sub_paths.append(tp.split(os.path.join(test_path, "test_"))[-1])

    src_paths = glob.glob(f'{src_path}/*.py')
    for sp in src_paths:
        if "__init__.py" in sp:
            continue
        if sp.split(src_path)[-1] not in test_sub_paths:
            raise Exception("no test for file " + sp)


def _update_requirements(**kwargs):
    """
    Update all requirements to the newest available
    """

    if not shutil.which('pur'):
        print("Pur not available, run 'python tool setup' to install")
        exit(1)

    requirements = glob.glob('*/*requirements.txt', recursive=True)

    for r in requirements:
        print(f'Updating {r}')
        subprocess.run(f"pur -r {r}", shell=True, check=True)


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
            _check_requirements()

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
            _check_test_files(
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


def _clean(**kwargs):

    for path in glob.glob('**/__pycache__', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/*egg-info', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/.coverage', recursive=True):
        os.remove(path)

    for path in glob.glob('**/.*cache', recursive=True):
        shutil.rmtree(path)

    for path in glob.glob('**/requirements_model.txt', recursive=True):
        os.remove(path)

    for path in glob.glob('**/model.pickle', recursive=True):
        os.remove(path)


def _release(**kwargs):
    raise Exception("relase step not implemented")


def cli(commands=['test', 'setup']):

    parser = argparse.ArgumentParser(description='Tool')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_setup = subparsers.add_parser('setup', help='setup help')
    parser_setup.set_defaults(func=_setup)

    parser_test = subparsers.add_parser('test', help='test help')
    parser_test.set_defaults(func=_test)

    parser_test.add_argument(
        '--no-requirements',
        dest='requirements',
        action='store_false',
        help='run requirements check'
    )

    parser_test.add_argument(
        '--no-pep8',
        dest='pep8',
        action='store_false',
        help='run unittests'
    )

    parser_test.add_argument(
        '--no-static',
        dest='static',
        action='store_false',
        help='run unittests'
    )

    parser_test.add_argument(
        '--no-license',
        dest='license',
        action='store_false', help='run unittests')

    parser_test.add_argument(
        '--no-test_files',
        dest='test_files',
        action='store_false',
        help='run unittests')

    parser_test.add_argument(
        '--no-unittests',
        dest='unittests',
        action='store_false',
        help='run unittests')

    parser_setup = subparsers.add_parser('clean', help='setup help')
    parser_setup.set_defaults(func=_clean)

    parser_setup = subparsers.add_parser('update', help='setup help')
    parser_setup.set_defaults(func=_update_requirements)

    parser_setup = subparsers.add_parser('release', help='setup help')
    parser_setup.set_defaults(func=_release)

    return parser.parse_args()


if __name__ == '__main__':

    args = cli()
    args.func(**vars(args))
