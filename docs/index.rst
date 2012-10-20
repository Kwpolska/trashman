Trashman.  A Python trash manager.
==================================

.. note:: This documentation is for Trashman version |release|.  Some parts of this documentation might not apply to other versions.

Trashman is a trash manager, i.e. an application which manages
trash folders.  It provides several backends.

How to use
----------
Install it from PyPI or the AUR.

To trash a file, just type ``trash FILE [FILE ...]`` into your shell.  To restore a file from the trash, add the ``-r`` (``--restore``) argument.  To empty the trash and delete the files forever, use the ``-e`` (``--empty``) switch.  Verbose output can be provided by ``-v`` (``--verbose``). The location of your trash will be printed by ``-w`` (``--trash-location``) and the files location will be presented by ``-W`` (``--files-location``); *w* as in where.  Other switches, related to Trashman, are ``-V`` (``--version``) and ``-h`` (``--help``).

Features
--------

Currently implemented in most backends:

 * trashing
 * trash conflict resolution
 * restore
 * localization support
 * tests

Not yet ready:

 * restore to inexisting directory (KDE refuses to do that, so we’ll probably do so, too)

Useless features that are planned:

 * CLI
 * Qt GUI

Developers using Trashman as a library may want to look at the :doc:`Global functions list <functions>` or :doc:`Backends info <backends/backends>` (and maybe :doc:`TODO`).  Other people may want to look at the :doc:`README <README>`.

Additional documents, indices and tables
----------------------------------------

.. toctree::
   :maxdepth: 2
   :numbered:

   trashman
   README for Trashman <README>
   functions
   backends/backends
   CONTRIBUTING
   LICENSE
   CHANGELOG
   TODO

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
