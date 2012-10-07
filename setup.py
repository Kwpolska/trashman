#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='trashman',
      version='1.0.4',
      description='A Python trash manager.',
      author='Kwpolska',
      author_email='kwpolska@kwpolska.tk',
      url='https://github.com/Kwpolska/trashman',
      license='3-clause BSD',
      long_description=open('README.rst').read(),
      platforms='any',
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
      packages=['trashman', 'trashman.backends'],
      scripts=['bin/trash'],
      data_files=[('share/man/man8', ['docs/trashman.8.gz']),
                  ('share/locale/en/LC_MESSAGES', ['locale/en/LC_MESSAGES/\
trashman.mo']),
                  ('share/locale/pl/LC_MESSAGES', ['locale/pl/LC_MESSAGES/\
trashman.mo']),
                  ('share/zsh/site-functions', ['shell-completions/_trash'])])
