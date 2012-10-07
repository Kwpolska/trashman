#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Trashman v1.0.4
# A Python trash manager.
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

    A Python trash manager.

    :Copyright: © 2011-2012, Kwpolska.
    :License: BSD (see /LICENSE).
"""

__title__ = 'Trashman'
__version__ = '1.0.4'
__author__ = 'Kwpolska'
__license__ = '3-clause BSD'
__docformat__ = 'restructuredtext en'

import sys
import os
import gettext

__pyver__ = sys.version_info

G = gettext.translation('trashman', '/usr/share/locale', fallback='C')
_ = G.gettext


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


### TMError         errors raised here      ###
class TMError(Exception):
    """Exceptions raised by the Trashman."""

    def __init__(self, src, info, msg):
        """TMError init."""
        DS.log.error('(auto TMError       ) [{}/{}]'.format(src, info) + msg)
        self.src = src
        self.info = info
        self.msg = msg

    def __str__(self):
        """You want to see error messages, don’t you?"""
        return self.msg

from .tmds import TMDS
DS = TMDS()
