#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v0.2.4
# A Python XDG trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
    trashman
    ~~~~~~~~

    A Python XDG trash manager.

    :Copyright: (C) 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

import shutil
import os
import os.path
import subprocess
import datetime
import sys
import argparse
import gettext

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

if os.getenv('XDG_DATA_HOME') is None:
    trash = os.path.expanduser("~/.local/share/Trash")
else:
    trash = os.getenv('XDG_DATA_HOME') + '/Trash'

T = gettext.translation('trashman', '/usr/share/locale', fallback='C')
_ = T.gettext

__title__ = 'Trashman'
__version__ = '0.2.4'
__author__ = 'Kwpolska'
__license__ = '3-clause BSD'


def size_dir(sdir):
    """Get the size of a directory.  Based on code found online."""
    size = os.path.getsize(sdir)

    for item in os.listdir(sdir):
        item = os.path.join(sdir, item)

        if os.path.isfile(item):
            size = size + os.path.getsize(item)
        elif os.path.isdir(item):
            size = size + size_dir(item)

    return size


def regenerate_trash():
    """Regenerate the trash.  Also used to re-create metadata."""
    zerosize = False

    if not os.path.exists(trash):
        os.mkdir(trash)
        zerosize = True

    if ((not os.path.exists(trash + '/files')) or
            (not os.path.exists(trash + '/info'))):
        os.mkdir(trash + '/files')
        os.mkdir(trash + '/info')
        zerosize = True
    if not zerosize:
        trashsize = size_dir(trash + '/files') + size_dir(trash + '/info')
    else:
        trashsize = 0

    infofile = '[Cached]\nSize=' + str(trashsize) + '\n'
    open(trash + '/metadata', "w").write(infofile)


def empty_trash(verbose):
    """Empty the trash."""
    shutil.rmtree(trash + '/files')
    shutil.rmtree(trash + '/info')
    regenerate_trash()
    if verbose:
        sys.stderr.write(_("emptied the trash\n"))


def list_files():
    """List the trash contents (using /bin/ls)."""
    subprocess.call('/bin/ls -CFG --color=auto ' + trash + '/files',
                    shell=True)


def move_to_trash(filepath, verbose):
    """Move specified file to trash."""
    # Filename alteration
    filename = os.path.basename(filepath)
    fileext = os.path.splitext(filename)

    tomove = filename
    collision = True
    i = 1

    while collision:
        if os.path.lexists(trash + '/files/' + tomove):
            tomove = fileext[0] + ' ' + str(i) + fileext[1]
            i = i + 1
        else:
            collision = False

    infofile = """[Trash Info]
Path={0}
DeletionDate={1}
""".format(os.path.realpath(filepath),
           datetime.datetime.now().strftime('%Y-%m-%dT%H:%m:%S'))

    os.rename(filepath, trash + '/files/' + tomove)

    open(trash + '/info/' + tomove + '.trashinfo',
         'w').write(infofile)

    regenerate_trash()

    if verbose:
        sys.stderr.write(_("trashed ‘{0}’\n").format(filename))


def restore_from_trash(filename, verbose):
    """Restores a file from trash."""
    infofile = configparser.ConfigParser()
    if infofile.read(trash + '/info/' + filename + '.trashinfo') != []:
        info = infofile['Trash Info']
        os.rename(trash + '/files/' + filename, info['Path'])
        os.remove(trash + '/info/' + filename + '.trashinfo')
        regenerate_trash()
        if verbose:
            sys.stderr.write(_('restored {0} to {1} (trashed {2})\n'.format(
                filename, info['Path'], info['DeletionDate'])))
    else:
        raise Exception('no such file in trash')


def main():
    """The main routine."""
    parser = argparse.ArgumentParser(description=_("Trashman – a Python \
                                     XDG trash manager."))


    argopt = parser.add_argument_group(_('options'))
    argopr = parser.add_argument_group(_('operations'))

    parser.add_argument('-V', '--version', action='version',
                        version='Trashman v' + __version__)
    argopr.add_argument('-e', '--empty', action='store_true', default=False,
                        dest='empty', help=_("empty the trash and exit"))
    argopr.add_argument('-l', '--list', action='store_true', default=False,
                        dest='flist', help=_("list the files in trash and \
                                              exit"))
    argopr.add_argument('-r', '--restore', action='store_true', default=False,
                        dest='restore', help=_("restore FILE(s) from trash"))
    argopt.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help=_("explain what is being done"))
    argopr.add_argument('-w', '--trash-location', action='store_true',
                        default=False, dest='showloc', help=_("print the \
                        trash location and exit"))
    parser.add_argument('files', metavar=_("FILE"), action='store', nargs='*',
                        help=_("files to trash"))
    args = parser.parse_args()

    exit_notrash = False

    if not os.path.exists(trash):
        if args.verbose:
            sys.stderr.write(_("“{0}” does not exist, \
creating...").format(trash))

        regenerate_trash()

    if args.flist:
        list_files()
        exit_notrash = True

    if args.empty:
        empty_trash(args.verbose)
        exit_notrash = True

    if args.showloc:
        print(trash)
        exit_notrash = True

    if args.restore:
        for fileres in args.files:
            restore_from_trash(fileres, args.verbose)
        exit_notrash = True

    if exit_notrash:
        exit()
    else:
        # Did not exit?  We can trash.
        for filedel in args.files:
            move_to_trash(filedel, args.verbose)
