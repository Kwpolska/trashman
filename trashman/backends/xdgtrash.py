#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
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

from .. import DS, _, TMError, size_dir
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

    try:
        if not os.path.exists(trashdir):
            os.mkdir(trashdir)
    except OSError:
        DS.error('Couldn’t access the proper directory, temporary trash \
is in in /tmp/TRASH')
        trashdir = os.path.join('tmp' 'TRASH')

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

    def list(self, human=True):
        """List the trash contents."""
        if human:
            self.log('listing contents (on stdout; human=True)')
        else:
            self.log('listing contents (return; human=False)')
        dirs = []
        files = []
        for f in os.listdir(self.filedir):
            if os.path.isdir(self.filedir + f):
                dirs.append(f)
            else:
                files.append(f)

        dirs.sort()
        files.sort()

        allfiles = []

        for i in dirs:
            allfiles.append(i + '/')

        for i in files:
            allfiles.append(i)

        if human:
            if allfiles != []:
                print('\n'.join(allfiles))
        else:
            return allfiles

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

    def restore(self, filename, verbose, tocwd=False):
        """Restore a file from trash."""
        self.log('restoring file {} (verbose={}, tocwd={})'.format(filename,
                 verbose, tocwd))
        info = configparser.ConfigParser()
        if os.path.exists(os.path.join(self.filedir, filename)):
            info.read(os.path.join(self.infodir, filename + '.trashinfo'))
            restname = os.path.basename(info.get('Trash Info', 'Path'))

            if tocwd:
                restdir = os.path.abspath('.')
            else:
                restdir = os.path.dirname(info.get('Trash Info', 'Path'))

            restfile = os.path.join(restdir, restname)
            if not os.path.exists(restdir):
                raise TMError('restore', 'nodir', _('no such directory: {}'
                              ' -- cannot restore').format(restdir))
            os.rename(os.path.join(self.filedir, filename), restfile)
            os.remove(os.path.join(self.infodir, filename + '.trashinfo'))
            self.regenerate()
            self.log('restored {} to {}'.format(filename, restfile))
            if verbose:
                sys.stderr.write(_('restored {} to {}\n').format(filename,
                                 restfile))

        else:
            self.log('couldn\'t find {} in trash'.format(filename))
            raise TMError('restore', 'nofile', _('no such file in trash'))
