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
# core.network Networking related module
#

import asyncio
import websockets
from tuxemon_server.core.network import parser
from tuxemon_server.core import event

class Server(object):
    def __init__(self, host='localhost', port=8765):
        self._server = websockets.serve(self.handler, host, port)
        self._connected = set()

    def listen(self):
        asyncio.get_event_loop().run_until_complete(self._server)
        asyncio.get_event_loop().run_forever()

    async def handler(self, websocket, path):
        # Register.
        self._connected.add(websocket)
        try:
            data = await websocket.recv()
            parsed_data = parser.parse(data)
            if parsed_data:
                print("Data successfully parsed!")
                response = event.event_pool.dispatch(parsed_data)
                await websocket.send(response)
            else:
                await websocket.send("Malformed client event: " + str(data))
        finally:
            # Unregister.
            self._connected.remove(websocket)

    def handle_event(self, event):
        return event.event_pool.dispatch(event)


if __name__ == "__main__":
    server = Server()
    server.listen()

#start_server = websockets.serve(hello, 'localhost', 8765)
#
#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()
