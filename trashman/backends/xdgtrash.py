#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.0
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.backends.xdgtrash
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    An XDG trash implementation.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

from .. import _, TMError, size_dir
from .trash import Trash
import shutil
import os
import os.path
import datetime
import sys
import logging

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


### XDGTrash       XDG trash backend       ###
class XDGTrash(Trash):
    """XDG trash backend."""

    if os.getenv('XDG_DATA_HOME') is None:
        trashdir = os.path.expanduser('~/.local/share/Trash')
    else:
        trashdir = os.getenv('XDG_DATA_HOME') + '/Trash'

    filedir = trashdir + '/files/'
    infodir = trashdir + '/info/'
    logger = logging.getLogger('XDGTrash')

    def regenerate(self):
        """Regenerate the trash and recreate metadata."""
        self.log('regenerating')
        zerosize = False

        if not os.path.exists(self.trashdir):
            os.mkdir(self.trashdir)
            zerosize = True

        if ((not os.path.exists(self.filedir)) or
                (not os.path.exists(self.infodir))):
            os.mkdir(self.filedir)
            os.mkdir(self.infodir)
            zerosize = True
        if not zerosize:
            trashsize = (size_dir(self.filedir) + size_dir(self.infodir))
        else:
            trashsize = 0

        infofile = '[Cached]\nSize=' + str(trashsize) + '\n'
        fh = open(os.path.join(self.trashdir, 'metadata'), 'w')
        fh.write(infofile)
        fh.close()

    def empty(self, verbose):
        """Empty the trash."""
        self.log('emptying (verbose={})'.format(verbose))
        shutil.rmtree(self.filedir)
        shutil.rmtree(self.infodir)
        self.regenerate()
        if verbose:
            sys.stderr.write(_('emptied the trash\n'))

    def list(self):
        """List the trash contents."""
        self.log('listing contents (on stdout)')
        dirs = []
        files = []
        for f in os.listdir(self.filedir):
            if os.path.isdir(self.filedir + f):
                dirs.append(f)
            else:
                files.append(f)

        dirs.sort()
        files.sort()

        for i in dirs:
            print(i + '/')

        for i in files:
            print(i)

    def trash(self, filepath, verbose):
        """Move specified file to trash."""
        self.log('trashing file {} (verbose={})'.format(filepath, verbose))
        # Filename alteration, a big mess.
        filename = os.path.basename(filepath)
        fileext = os.path.splitext(filename)

        tomove = filename
        collision = True
        i = 1

        while collision:
            if os.path.lexists(self.filedir + tomove):
                tomove = fileext[0] + ' ' + str(i) + fileext[1]
                i = i + 1
            else:
                collision = False

        infofile = """[Trash Info]
Path={}
DeletionDate={}
""".format(os.path.realpath(filepath),
           datetime.datetime.now().strftime('%Y-%m-%dT%H:%m:%S'))

        os.rename(filepath, self.filedir + tomove)

        f = open(os.path.join(self.infodir, tomove + '.trashinfo'), 'w')
        f.write(infofile)
        f.close()

        self.regenerate()

        if verbose:
            sys.stderr.write(_('trashed \'{}\'\n').format(filename))

    def restore(self, filename, verbose):
        """Restore a file from trash."""
        self.log('restoring file {} (verbose={})'.format(filename, verbose))
        info = configparser.ConfigParser()
        if os.path.isfile(os.path.join(self.filedir, filename)):
            info.read(os.path.join(self.infodir, filename + '.trashinfo'))
            os.rename(os.path.join(self.filedir, filename),
                      info.get('Trash Info', 'Path'))
            os.remove(os.path.join(self.infodir, filename + '.trashinfo'))
            self.regenerate()
            self.log('restored {} to {}'.format(filename,
                     info.get('Trash Info', 'Path')))
            if verbose:
                sys.stderr.write(_('restored {} to {}\n').format(filename,
                                 info.get('Trash Info', 'Path')))

        else:
            self.log('couldn\'t find {} in trash'.format(filename))
            raise TMError(_('no such file in trash'))