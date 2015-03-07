========
Backends
========
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2011–2015, Chris Warrick.
:License: BSD (see /LICENSE or :doc:`Appendix B <LICENSE>`.)
:Date: 2015-02-28
:Version: 1.5.0

.. index:: backends

Trashman uses backends for managing files.  All the backends define the same
functions and inherit from the Trash class.

Backend requirements:
 * name ending in Trash (eg. XDGTrash, DummyTrash)
 * PEP 8, docstrings
 * inherit from Trash
 * throw exceptions and log activity
 * implement the functions listed below (do not re-implement ``log`` unless needed)
 * do actual work (save for the ``dummy`` backend)
 * have a ``self.trashdir`` variable with the trash location (``None`` if impossible)
 * have a ``self.logger`` instance (``import logging``, ``logging.getLogger('NAME')``

In order to choose a backend, use ``trashman.backends.select(backend)``.  If ``backend`` is ``auto``, a choice will be made basing on the config, and if it also says auto, on the OS used.  If it is ``list``, a human-readable list of backends will be printed.

Functions
=========
(this automatically-generated of the Trash class.)

.. currentmodule:: trashman.backends.trash

.. autoclass:: trashman.backends.trash.Trash
   :members:

Existing backends
=================
 .. toctree::
    :maxdepth: 2
    :numbered:

    /backends/dummytrash
    /backends/xdgtrash
