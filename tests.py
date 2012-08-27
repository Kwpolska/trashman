#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Trashman test suite
# Copyright (C) 2012, Kwpolska.
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

import unittest
import os

import trashman
import trashman.tmds
import trashman.backends
import trashman.backends.trash
import trashman.backends.dummytrash
import trashman.backends.xdgtrash


class TestTM(unittest.TestCase):
    # trashman
    def test_size_dir(self):
        req = trashman.size_dir('./bin/')
        if req != 4227:  # Hardcoded, but the size shouldn’t change.
            raise Exception('test_size_dir: size != 4227')

    def test_tmds(self):
        tmds = trashman.tmds.TMDS()
        req = tmds.config.get('default_backend', 'name')
        tmds.log.debug('PB unittest/TestPB is running now on this machine.')

    def test_backends(self):
        trashman.backends.select('auto')
        trashman.backends.select('dummy')
        trashman.backends.select('xdg')

    def test_backends_DummyTrash(self):
        try:
            t = trashman.backends.dummytrash.DummyTrash()
            t.logquiet = True
            t.log('DummyTrash logging test')
            t.regenerate()
            t.trash('TRASHTESTFILE', False)
            t.restore('TRASHTESTFILE', False)
            t.empty(False)
        except NotImplementedError:
            print('NotImplementedError: backend didn’t implement \
something it should.')
            os.remove('TRASHTESTFILE')

    def test_backends_XDGTrash(self):
        try:
            t = trashman.backends.xdgtrash.XDGTrash()
            t.log('XDGTrash logging test')
            t.regenerate()

            f = open('./TRASHTESTFILE', 'w')
            f.write('trashman')
            f.close()
            b = open('./TRASHTESTFILE')
            if b.read() != 'trashman':
                raise Exception('cannot read TRASHTESTFILE @ b1')
            b.close()

            t.trash('TRASHTESTFILE', False)
            a = open(os.path.join(t.filedir, 'TRASHTESTFILE'))
            if a.read() != 'trashman':
                raise Exception('cannot read TRASHTESTFILE @ a1')
            a.close()

            t.restore('TRASHTESTFILE', False)
            b = open('./TRASHTESTFILE')
            if b.read() != 'trashman':
                raise Exception('cannot read TRASHTESTFILE @ b2')
            b.close()

            os.remove('./TRASHTESTFILE')
        except NotImplementedError:
            print('NotImplementedError: backend didn’t implement \
something it should.')
            os.remove('./TRASHTESTFILE')

if __name__ == '__main__':
    unittest.main()
