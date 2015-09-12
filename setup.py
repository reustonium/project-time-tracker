#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='project-time-tracker',
    version='0.1.0',
    description="CLI for easily tracking how much time you spend on each project",
    long_description=readme + '\n\n' + history,
    author="Andy Ruestow",
    author_email='andy@ruestow.me',
    url='https://github.com/reustonium/project-time-tracker',
    packages=[
        'project-time-tracker',
    ],
    package_dir={'project-time-tracker':
                 'project-time-tracker'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='project-time-tracker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
