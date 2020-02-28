#! /usr/bin/env python3
# encoding: utf-8

import glob
import os
import shutil
import subprocess


def check_requirements():
    """
    Check that all requirements in the environment corresponds to what is
    specified in the requirement files.
    """

    requirements = glob.glob('*/*requirements.txt', recursive=True)

    for r in requirements:
        subprocess.run(f"requirementz --file {r}", shell=True, check=True)


def check_test_files(src_path, test_path):
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


def update_requirements():
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
