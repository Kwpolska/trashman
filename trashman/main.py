#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.3
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.main()
    ~~~~~~~~~~~~~~~

    Trashman’s main routine.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

from . import DS, _, __version__
from .backends import select
import argparse


### main()         The main routine        ###
def main():
    """The main routine."""
    parser = argparse.ArgumentParser(description=_('Trashman -- a Python \
                                     trash manager.'))

    argopt = parser.add_argument_group(_('options'))
    argopr = parser.add_argument_group(_('operations'))

    parser.add_argument('-V', '--version', action='version',
                        version='Trashman v' + __version__, help=_('show \
                        version number and quit'))

    argopt.add_argument('-v', '--verbose', action='store_true', default=False,
                        dest='verbose', help=_('explain what is being done'))
    argopt.add_argument('-b', '--backend', action='store', default='config',
                        dest='backend', help=_('select the backend (default: \
                        config->auto->xdg)'))

    argopr.add_argument('-e', '--empty', action='store_true', default=False,
                        dest='empty', help=_('empty the trash and quit'))
    argopr.add_argument('-l', '--list', action='store_true', default=False,
                        dest='flist', help=_('list the files in trash and \
                                              quit'))
    argopr.add_argument('-r', '--restore', action='store_true', default=False,
                        dest='restore', help=_('restore FILE(s) from trash'))
    argopr.add_argument('-w', '--trash-location', action='store_true',
                        default=False, dest='showtloc', help=_('print the \
                        trash location and quit'))
    argopr.add_argument('-W', '--files-location', action='store_true',
                        default=False, dest='showfloc', help=_('print the \
                        trashed files location and quit'))
    parser.add_argument('files', metavar=_('FILE'), action='store', nargs='*',
                        help=_('files to trash'))
    args = parser.parse_args()

    quit_notrash = False

    select(args.backend)
    if args.backend == 'info':
        quit_notrash = True
    else:
        DS.trash.regenerate()

    if args.flist:
        DS.trash.list()
        quit_notrash = True

    if args.showtloc:
        print(DS.trash.trashdir)
        quit_notrash = True

    if args.showfloc:
        print(DS.trash.filedir)
        quit_notrash = True

    if args.restore:
        for fileres in args.files:
            DS.trash.restore(fileres, args.verbose)
        quit_notrash = True

    if args.empty:
        DS.trash.empty(args.verbose)
        quit_notrash = True

    if quit_notrash:
        exit()
    else:
        # Did not quit?  We can trash.
        for filedel in args.files:
            DS.trash.trash(filedel, args.verbose)
