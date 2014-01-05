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

import socket
import ssl

from .listener import listen, Callback
from .lib import identify


class Client:
    def __init__(self, nick="iircBot", server="chat.freenode.net", port=6667, ident=None, ssl=False, ipv6=False):
        self.nick = nick
        self.server = server
        self.port = port
        self.ssl = ssl
        self.ident = ident
        self.ipv6 = ipv6
        self.listeners = []

    def start(self):
        """
        Starts the IRC bot.
        """
        if self.ipv6:
            self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        else:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s = self.s
        s.connect((self.server, self.port))

        if self.ssl:
            self.s = ssl.wrap_socket(s)

        if self.ident:
            identify(s, self.ident) # Identify to services

        listen(s) # Call the listen function to start listening on the socket

    def on(self, event, c):
        l = Callback(event, c)
        self.listeners.append(l)
