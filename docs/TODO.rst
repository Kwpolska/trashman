=================
TODO for Trashman
=================
:Author: Kwpolska
:Copyright: See Appendix A.
:Date: 2012-08-27
:Version: 1.0.1

.. index:: TODO

  * de_DE

    requires: yours truly.

  * restore files with help

    requires: magic, see kwsblog/modify/color for a cheap solution.

  * restore with better handling of errors AND handling of getting a
        file from a subdirectory

    requires: time.

    NOTE: KDE (the implementation I’m basing some of mine on) doesn’t
    like doing the second thing.  Error message pasted verbatim:

          > The directory /home/kwpolska/Desktop/TRASHTEST does not exist
          > anymore, so it is not possible to restore this item to its
          > original location.  You can either recreate that directory
          > and use the restore operation again, or drag the item
          > anywhere else to restore it.

          (created a directory called ~/Desktop/TRASHTEST, added a
          file, trashed the directory, tried to restore the file
          inside)

  * [proposition] file management UI

    requires: magic, qt/ncurses (ranger is in python, this might be
        of use)

    NOTE: don’t forget that ncurses = pure evil!

    UPDATE: ranger uses ncurses...

-- Kwpolska 2012-08-25T17:40:00Z
