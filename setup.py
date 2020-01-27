#! /usr/bin/env python3
# encoding: utf-8

import io

from setuptools import setup, find_packages

with io.open('README.rst', encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='dummy',
    use_scm_version=True,
    description=("Template python module."),
    long_description=long_description,
    url='https://github.com/energinet-open/python_module_template',
    author='Energinet',
    author_email='XYZ@energinet.dk',
    license='Apache License Version 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': ['dummy=dummy.__main__:run'],
    },
    keywords=('template', 'boilerplate'),
    packages=find_packages(where='src', exclude=['test']),
    package_dir={"": "src"},
    install_requires=['', ],
    extras_require={
        'tests': ['pytest', 'pytest_cov', 'mypy', 'pytest-mypy',
                  'flake8'],
        'develop': ['', ]
        },
)
