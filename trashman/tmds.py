#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.TMDS
    ~~~~~~~~~~~~~
    Trashman Data Storage.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

from . import __version__
import sys
import os
import logging
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


### TMDS           TM global data storage  ###
class TMDS(object):
    """Trashman Data Storage."""
    trash = None
    trashdir = None

    # Creating the configuration/log stuff...
    if sys.platform == 'darwin':
        confhome = os.path.expanduser('~/Library/Application Support/')
    else:
        confhome = os.getenv('XDG_CONFIG_HOME')
        if confhome is None:
            confhome = os.path.expanduser('~/.config/')

    kwdir = os.path.join(confhome, 'kwpolska')
    confdir = os.path.join(kwdir, 'trashman')

    if not os.path.exists(confhome):
        os.mkdir(confhome)

    if not os.path.exists(kwdir):
        os.mkdir(kwdir)

    if not os.path.exists(confdir):
        os.mkdir(confdir)

    if not os.path.exists(confdir):
        error(_('Cannot create the configuration directory.'))
        exit(1)

    config = configparser.SafeConfigParser()
    config.read(os.path.join(confdir, 'trashman.cfg'))
    if not config.has_section('default_backend'):
        config.add_section('default_backend')
        config.set('default_backend', 'name', 'auto')
        config.write(open(os.path.join(confdir, 'trashman.cfg'), 'w'))

    if not os.path.exists(confdir):
        try:
            os.mkdir(confdir)
        except:
            try:
                os.mkdir(confhome)
            except:
                pass

            try:
                os.mkdir(os.path.join(confhome, 'kwpolska'))
                os.mkdir(confdir)
            except:
                self.error('Cannot create the config directory ({}).'.format(
                    confdir))

    logging.basicConfig(format='%(asctime)-15s [%(levelname)-7s] \
:%(name)-10s: %(message)s', filename=confdir + '/trashman.log',
                        level=logging.DEBUG)
    log = logging.getLogger('trashman')

    log.info('*** Trashman v{}'.format(__version__))

    def info(self, msg):
        """Show an information and log it."""
        sys.stderr.write('* {}'.format(msg))
        self.log.info('(auto info    ) {}'.format(msg))

    def warning(self, msg):
        """Show a warning and log it."""
        sys.stderr.write('! {}'.format(msg))
        self.log.warning('(auto warning ) {}'.format(msg))

    def error(self, msg):
        """Show an error and log it."""
        sys.stderr.write('E {}'.format(msg))
        self.log.error('(auto error   ) {}'.format(msg))

    def critical(self, msg):
        """Show a critical error and log it."""
        sys.stderr.write('C {}'.format(msg))
        self.log.critical('(auto critical) {}'.format(msg))
