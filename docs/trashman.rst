=========
Trashman
=========

:Author: Kwpolska <kwpolska@kwpolska.tk>
:Copyright: See Appendix A.
:Date: 2012-08-13
:Version: 0.2.1
:Manual section: 1
:Manual group: Trashman manual

SYNOPSIS
========

*trashman* <operation> [options] [targets]

DESCRIPTION
===========

Trashman is a XDG trash manager, i.e. an application which manages
trash folders used by most modern-day non-proprietary desktops.


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
    Prints the trash location.

OPTIONS
=======

**-v, --verbose**
    Turns on verbose mode.

**-V, --version**
    Prints the version in use.

EXAMPLES
========

trash .gnome
    Trashes the .gnome directory.

trash -r .gnome
    Restores the .gnome directory from trash

trash -e
    Empties the trash.

(GNOME, especially in version 3, is a huge pile of crap.)

BUGS
====
Bugs should be reported at the GitHub page
(<https://github.com/Kwpolska/trashman/issues>).  You can also
send mail to <kwpolska@kwpolska.tk>.
