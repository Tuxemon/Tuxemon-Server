#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon Server
# Copyright (C) 2016, William Edwards <shadowapex@gmail.com>,
#                     Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon.
#
# Tuxemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tuxemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tuxemon.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# William Edwards <shadowapex@gmail.com>
#
#
# tuxemon_headless.py Main game
#

import json
import time
from neteria.client import NeteriaClient

if __name__ == "__main__":
    # Create a client instance.
    client = NeteriaClient()
    client.listen()

    # Discover a Neteria Server.
    print "Discovering Neteria servers..."
    while not client.registered:
        client.autodiscover()
        time.sleep(1)
    print "Connected!"

    # Send data to the server.
    exit_cmds = ['quit', 'exit']
    data = None
    while data not in exit_cmds:
        try:
            data = str(raw_input("> "))
            data = json.loads(data)
        except Exception as e:
            print("Error decoding client command: %s" % str(e))
            data = ""
        if data:
            client.event(data)

