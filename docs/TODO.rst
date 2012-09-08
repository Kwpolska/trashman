=================
TODO for Trashman
=================
:Author: Kwpolska
:Copyright: See Appendix A.
:Date: 2012-09-08
:Version: 1.0.3

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

        The directory /home/kwpolska/Desktop/TRASHTEST does not exist
        anymore, so it is not possible to restore this item to its
        original location.  You can either recreate that directory
        and use the restore operation again, or drag the item
        anywhere else to restore it.

  (created a directory called ~/Desktop/TRASHTEST, added a
  file, trashed the directory, tried to restore the file
  inside)

* [proposition] file management UI

  requires: magic, qt/ncurses (ranger is in python, this might be
      of use)

  NOTE: don’t forget that ncurses = pure evil!

  UPDATE: ranger uses ncurses...

  MOCKUP (also exists in a qt designer .ui file on my local machine)::

    +-----------------------------------------------------------------------+
    | o o o                         Trashman                                |
    | File [Move Empty Restore Delete Quit] Backends [] Help [Online About] |
    | | /// |                    Trashman  v1.10                            |
    | | /// |   **1 item**                                                  |
    | | /// | ↓                 Copyright © 2011-2012 Kwpolska.             |
    | | /// |   666.0 MB                                                    |
    | \_____/                     Backend [ backend               ↓ ] [...] |
    |                                                                       |
    | +-------------------+-----------+-------------------+---------------+ |
    | | File              | Size      | Original Location | Date Deleted  | |
    | +-------------------+-----------+-------------------+---------------+ |
    | | > .gnome          | 666.0 MB  | /home/kwpolska/   | 2012-08-28T…  | |
    | | > WINDOWS         | 6666.0 MB | /media/windows/   | 2038-01-19T…  | |
    | +-------------------+-----------+-------------------+---------------+ |
    | [ Move to Trash ]     [ Empty ]            [ Restore ]     [ Delete ] |
    +-----------------------------------------------------------------------+

(that fancy thing in the top-left is a trash icon.  And the arror next to it
opens a menu, just like the [...] next to the backend combo box.)

-- Kwpolska 2012-08-28T18:17:00Z
