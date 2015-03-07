========
Trashman
========

:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2011–2015, Chris Warrick.
:License: BSD (see /LICENSE or Appendix B.)
:Date: 2015-03-07
:Version: 1.5.0
:Manual section: 1
:Manual group: Trashman manual

SYNOPSIS
========

*trashman* [-hVerlvwW] [FILE [FILE...]]

DESCRIPTION
===========

Trashman is a trash manager, i.e. an application which manages
trash folders.  It provides several backends.

OPERATIONS
==========

**[FILE [FILE...]]**
    Trashes the FILE(s).

**-e, --empty**
    Empties the trash.

**-r, --restore**
    Restores the FILE(s) from the trash.

**-l, --list**
    Lists the trash contents using ls.

**-w, --trash-location**
    Prints the trash root location.

**-W, --files-location**
    Prints the location of trashed files, which may be different from the root.

OPTIONS
=======

**-b BACKEND, --backend BACKEND**
    Selects the backend to use.  'auto' chooses the backend automatically
    (fallback: XDG), 'config' tries the config file (which is 'auto' by
    default) and 'list' displays a list of the possible backends.  Can be
    configured in  **~/.config/kwpolska/trashman/trashman.cfg**.

**-h, --help**
    Prints a help message.

**-v, --verbose**
    Turns on verbose mode.

**-V, --version**
    Prints the version in use.

EXAMPLES
========

trash foo
    Trashes the ``foo`` directory.

trash foo
    Restores the ``foo`` directory from trash.

trash -e
    Empties the trash.

BUGS
====
Bugs should be reported at the GitHub page
(<https://github.com/Kwpolska/trashman/issues>).  You can also
send mail to <chris@chriswarrick.com>.
