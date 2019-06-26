# -*- coding: utf-8; mode: python -*-

# Copyright (C) 2017 Johannes Grassler <johannes@btw23.de>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301, USA.

import signal
import traceback
import threading

signal_event = threading.Event()
signal_received = None

def handler(signum, frame):
    global signal_event   # used for interruptable sleep
    signal_event.set()
    global signal_received
    signal_received = signum

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)
