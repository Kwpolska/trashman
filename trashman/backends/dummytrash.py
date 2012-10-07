#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.backends.dummytrash
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    A dummy backend, printing all the requests it gets.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""
import logging


### DummyTrash     A dummy trash           ###
class DummyTrash(object):
    """
    A dummy trash, printing and logging actions
    that would be performed.
    """

    trashdir = None
    filedir = None
    infodir = None
    logger = logging.getLogger('DummyTrash')
    logquiet = False

    def log(self, msg, lvl='debug'):
        """Log a message."""
        if not self.logquiet:
            print('DummyTrash: {}'.format(msg))

        if lvl != 'debug':
            raise NotImplementedError

        self.logger.debug(msg)

    def regenerate(self):
        """Regenerate the trash and recreate metadata."""
        self.log('regenerating')

    def empty(self, verbose):
        """Empty the trash."""
        self.log('emptying (verbose={})'.format(verbose))
        self.regenerate()

    def list(self, human=True):
        """List the trash contents."""
        if human:
            self.log('listing contents (on stdout; human=True)')
        else:
            self.log('listing contents (return; human=False)')

    def trash(self, filepath, verbose):
        """Move specified file to trash."""
        self.log('trashing file {} (verbose={})'.format(filepath, verbose))

    def restore(self, filename, verbose):
        """Restore a file from trash."""
        self.log('restoring file {} (verbose={})'.format(filename, verbose))
