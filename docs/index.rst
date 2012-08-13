Trashman.  A Python XDG trash manager.
======================================

.. note:: This documentation is for Trashman version |release|.  Some parts of this documentation might not apply to other versions.

Trashman is a trash manager, conforming to XDG standards.  It is a work-in-progress, though, and it may break.

How to use
----------
Install it from PyPI or the AUR.

To trash a file, just type ``trash FILE [FILE ...]`` into your shell.  To restore a file from the trash, add the ``-r`` (``--restore``) argument.  To empty the trash and delete the files forever, use the ``-e`` (``--empty``) switch.  Verbose output can be provided by ``-v`` (``--verbose``) and the location of your Trash will be printed by ``-w`` (``--trash-location``, *w* as in where.)  Other switches, related to Trashman, are ``-V`` (``--version``) and ``-h`` (``--help``).

Features
--------

Currently implemented:

 * basic trashing
 * trash conflict resolution
 * restore

Not yet ready:

 * tests
 * restore to inexisting directory (KDE refuses to do that, so it isn’t hard to do)
 * localizations

Useless features that are planned:

 * CLI
 * Qt GUI

Developers using Trashman as a library may want to look at the :doc:`Functions list. <functions>`  Other people may want to look at the :doc:`README <README>`.

Additional documents, indices and tables
----------------------------------------

.. toctree::
   :maxdepth: 2

   trashman
   functions
   README for Trashman <README>
   LICENSE

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
