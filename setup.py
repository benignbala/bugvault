#!/usr/bin/python

from setuptools import setup, find_packages

setup (
    name = 'bugvault',
    version = '0.1',
    url='http://github.com//sandman/',
    license='Apache Software License v2',
    author="Balachandran S <balachandran@balachandran.org>, Abhisek Kumar Rout <abhisek.rout93@gmail.com>"
    install_requires=['Flask>=0.10.1',
                      'Flask-SQLAlchemy>=2.0',
                      'SQLAlchemy>=1.0.8',
                      'pytest'
                  ],
    description='A simple, usable bug tracking system'
    long_description=open("README.adoc").read()
    packages=['bugvault'],
    include_package_data=True,
    platforms='any',
)
