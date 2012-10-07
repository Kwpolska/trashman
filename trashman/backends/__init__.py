#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
# A Python trash manager.
# Copyright (C) 2011-2012, Kwpolska.
# See /LICENSE for licensing information.

"""
    trashman.backends
    ~~~~~~~~~~~~~~~~~

    Backends for Trashman.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

from .. import DS, _, TMError, __pyver__
import importlib


def select(backend):
    """Select the backend.  'auto' for auto-selection and 'info' for list."""
    backend = backend.strip().lower()
    # internal: [log/human, module, class, 'description as in docs', humans?]
    BACKENDS = {'auto': ['', '', '', _('[choose automatically]'), True],
                'config': ['', '', '', _('[consult trashman.cfg]'), True],
                'list': ['', '', '', _('[list backends]'), False],
                'dummy': ['dummy', 'dummytrash', 'DummyTrash', _('A dummy \
backend, printing all the requests it gets.'), False],
                'xdg': ['XDG', 'xdgtrash', 'XDGTrash', _('An XDG trash \
implementation.'), True]}
    if backend == 'config':
        backend = DS.config.get('default_backend', 'name')
        DS.log.info(_('*** backend from config: {}').format(backend))

    if backend == 'auto':
        # XDG is the only usable backend right now.
        backend = 'xdg'
    elif backend == 'list':
        col1 = len(max(BACKENDS.keys(), key=len))
        col2p = []
        col3p = []

        if __pyver__[0] == 3:
            for k, i in BACKENDS.items():
                col2p.append(i[0])
                col3p.append(i[3])
        else:
            for k, i in BACKENDS.iteritems():
                col2p.append(i[0])
                col3p.append(i[3])

        idword = '-b'
        nameword = _('NAME')
        dword = _('DESCRIPTION')
        col2 = len(max(col2p, key=len))
        col3 = len(max(col3p, key=len))

        if len(idword) > col1:
            col1 = len(idword)

        if len(nameword) > col2:
            col2 = len(nameword)

        space1 = (col1 - len(idword)) * ' '
        space2 = (col2 - len(nameword)) * ' '

        print(' '.join([idword + space1, '|', nameword + space2, '|', dword]))
        print('-+-'.join([col1 * '-', col2 * '-', col3 * '-']))

        if __pyver__[0] == 3:
            for k, i in BACKENDS.items():
                space1 = (col1 - len(k)) * ' '
                space2 = (col2 - len(i[0])) * ' '
                print(' '.join([k + space1, '|', i[0] + space2, '|', i[3]]))
        else:
            for k, i in BACKENDS.iteritems():
                space1 = (col1 - len(k)) * ' '
                space2 = (col2 - len(i[0])) * ' '
                print(' '.join([k + space1, '|', i[0] + space2, '|', i[3]]))

    if backend != 'list':
        if backend not in BACKENDS.keys():
            raise TMError(_('No such backend: {}').format(backend))
        else:
            b = BACKENDS[backend]
            mn = b[1]
            mc = b[2]
            m = importlib.import_module('.backends.{}'.format(mn), 'trashman')
            DS.trash = eval('m.{}'.format(mc))()
            DS.trashdir = DS.trash.trashdir
            DS.log.info(_('*** using the {} backend').format(b[0]))
