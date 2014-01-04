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
    def __init__(self, nick="iirc_bot", server="chat.freenode.net", port=6667,
                 ident="iirc", realname="IIRC - Improved IRC", nickserv=None,
                 server_pass=None, ssl=False, ipv6=False):
        self.nick = nick
        self.server = server
        self.port = port
        self.ssl = ssl
        self.ident = ident
        self.realname = realname
        self.nickserv = nickserv
        self.server_pass = server_pass
        self.ipv6 = ipv6
        self.listeners = []

    def start(self):
        """
        Starts the IRC client.
        """
        if self.ipv6:
            self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        else:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s = self.s
        s.connect((self.server, self.port))

        # send USER and NICK to the server
        self.register()

        if self.ssl:
            self.s = ssl.wrap_socket(s)

        if self.nickserv is not None:
            identify(s, self.nickserv) # Identify to services

        listen(s) # Call the listen function to start listening on the socket

    def register(self):
        """
        Register with the IRC server.
        - Send a PASS command, if applicable.
        - Send a USER command: USER ident ident ident :realname
        - Send a NICK command: NICK nickname
        """
        if self.server_pass:
            self.s.send("PASS %s\n" % self.server_pass)
        self.s.send("USER %s %s %s :%s\n" % (self.ident, self.ident,
                                             self.ident, self.real_name))
        self.s.send("NICK %s\n" % self.nick)

    def on(self, event, c):
        l = Callback(event, c)
        self.listeners.append(l)
