=============================
Appendix E. TODO for Trashman
=============================
:Author: Kwpolska <kwpolska@kwpolska.tk>
:Copyright: © 2011-2012, Kwpolska.
:License: BSD (see /LICENSE or :doc:`Appendix B <LICENSE>`.)
:Date: 2012-10-07
:Version: 1.0.4

.. index:: TODO

* de_DE

  requires: yours truly.

* restore files with help

  requires: magic, see kwsblog/modify/color for a cheap solution.

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

(that fancy thing in the top-left is a trash icon.  And the arrow next to it
opens a menu, just like the [...] next to the backend combo box.)

-- Kwpolska 2012-09-22T12:30:00Z
