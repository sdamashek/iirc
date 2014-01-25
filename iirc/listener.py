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


class Event:
    """
    An event represents something happening on IRC, i.e. a message is received,
    someone parts the channel, etc.
    """
    def __init__(self, data):
        self.data = data
        self.on_receive()

    def on_receive(self):
        pass

    def get_data(self):
        return self.data


class JoinEvent(Event):
    """
    JoinEvents represent someone joining a channel.
    Data:
    * channel - a string representing the channel joined
    * source - a dictionary with keys nick, user, and host, representing the
               user that joined the channel
    """
    e_type = "join"


class PartEvent(Event):
    """
    PartEvents represent someone leaving a channel.
    Data:
    * channel - a string representing the channel parted
    * source - a dictionary with keys nick, user, and host, representing the
               user that left the channel
    * message - a string representing the part message/comment, or None if
                there wasn't a part message
    """
    e_type = "part"


class QuitEvent(Event):
    """
    QuitEvents represent someone quitting IRC.
    Data:
    * source - a dictionary with keys nick, user, and host, representing the
               user that quit
    * message - the quit message, or None of there wasn't one
    """
    e_type = "quit"


class KickEvent(Event):
    """
    KickEvents represent someone being kicked from IRC.
    Data:
    * channel - the channel
    * kicker - a dict with keys nick, user, and host, representing the op that
               kicked
    * kickee - a dict with keys nick, user, and host, representing the person
               who was kicked from the channel
    """
    e_type = "kick"


class ChanMsgEvent(Event):
    """
    ChanMsgEvents represent messages being sent to a channel.
    Data:
    * source - a dict with keys nick, user, and host, representing the sender
               of the message
    * channel - the channel the message was sent to
    * message - the actual message
    """
    e_type = "chanmsg"


class PrivMsgEvent(Event):
    """
    PrivMsgEvents represent messages sent to your bot/client.
    Data: same as ChanMsgEvent, but without channel
    """
    e_type = "privmsg"


class ChanNoticeEvent(Event):
    """
    ChanNoticeEvents represent notices being sent to a channel.
    Data:
    * source - a dict with keys nick, user, and host, representing the noticer
    * channel - the channel the notice was sent to
    * message - the message that is contained within the notice
    """
    e_type = "channotice"


class PrivNoticeEvent(Event):
    """
    PrivNoticeEvents represent notices being sent to your bot/client.
    Data: same as ChanNoticeEvent, except without channel
    """
    e_type = "privnotice"
