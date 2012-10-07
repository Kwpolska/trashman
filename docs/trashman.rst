========
Trashman
========

:Author: Kwpolska <kwpolska@kwpolska.tk>
:Copyright: © 2011-2012, Kwpolska.
:License: BSD (see /LICENSE or Appendix B.)
:Date: 2012-10-07
:Version: 1.0.4
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

trash .gnome
    Trashes the .gnome directory.

trash -r .gnome
    Restores the .gnome directory from trash.

trash -e
    Empties the trash.

(GNOME, especially in version 3, is a huge pile of crap.)

BUGS
====
Bugs should be reported at the GitHub page
(<https://github.com/Kwpolska/trashman/issues>).  You can also
send mail to <kwpolska@kwpolska.tk>.
