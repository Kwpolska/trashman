#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
#from distutils.core import setup

setup(name='trashman',
      version='0.2.0',
      description='A Python XDG trash manager.',
      author='Kwpolska',
      author_email='kwpolska@kwpolska.tk',
      url='https://github.com/Kwpolska/trashman',
      license='3-clause BSD',
      long_description=open('README.rst').read(),
      platforms='Arch Linux',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Utilities'],
      scripts=['bin/trash'])
