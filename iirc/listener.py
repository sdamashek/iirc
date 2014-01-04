#!/usr/bin/python3
# Copyright (C) 2013 Samuel Damashek, Fox Wilson, James Forcier
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

class Callback:
    """
    A Callback represents a function that is called when an event occurs.
    """
    def __init__(self, e_type, func):
        self.e_type = e_type
        self.func = func

    def __call__(self, event):
        if self.is_applicable(event):
            self.func(event)

    def is_applicable(self, event):
        """
        Checks to see if an event applies to this Callback.
        """
        return True
