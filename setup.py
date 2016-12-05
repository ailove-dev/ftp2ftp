#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]


setup(
    name='ftp2ftp',
    version='0.1.0',
    description="Ftp2ftp help you transfer files from one FTP server to another without storing files on running machine.",
    long_description=readme + '\n\n' + history,
    author="Alex Shalynin",
    author_email='a.shalynin@gmail.com',
    url='https://github.com/ailove-dev/ftp2ftp',
    packages=[
        'ftp2ftp',
    ],
    package_dir={'ftp2ftp':
                 'ftp2ftp'},
    entry_points={
        'console_scripts': [
            'ftp2ftp=ftp2ftp.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ftp2ftp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
