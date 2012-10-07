#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.backends.trash
    ~~~~~~~~~~~~~~~~~~~~~~~

    Base Trash class.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""
from .. import DS


### Trash          Base Trash class        ###
class Trash(object):
    """Base Trash class."""

    trashdir = None
    filedir = None
    infodir = None
    logger = DS.log

    def log(self, msg, lvl='debug'):
        """Log a message."""
        if lvl in ('debug', 'info', 'warning', 'error', 'critical'):
            eval('self.logger.{}(msg)'.format(lvl))
        else:
            DS.critical('SECURITY ALERT: Trash.log got a wrong level!')

    def regenerate(self):
        """Regenerate the trash and recreate metadata."""
        pass  # Some backends don’t need regeneration.

    def empty(self, verbose):
        """Empty the trash."""
        raise NotImplementedError(_('Backend didn’t \
implement this functionality'))

    def list(self, human=True):
        """List the trash contents."""
        raise NotImplementedError(_('Backend didn’t \
implement this functionality'))

    def trash(self, filepath, verbose):
        """Move specified file to trash."""
        raise NotImplementedError(_('Backend didn’t \
implement this functionality'))

    def restore(self, filename, verbose):
        """Restore a file from trash."""
        raise NotImplementedError(_('Backend didn’t \
implement this functionality'))
