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

import logging
import neteria.server
import neteria.tools
from tuxemon_server.core.transport import abstract_transport
from tuxemon_server.core import event

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class NeteriaTransport(abstract_transport.AbstractTransport):
    def __init__(self):
        self._middleware = neteria.tools._Middleware(self)
        self._server = None
        self._connected = set()

    def configure(self, parser, host='localhost', port=8765):
        self._server = neteria.server.NeteriaServer(self._middleware, server_address=host,
                                                    server_port=int(port))
        self._parser = parser

    def listen(self):
        self._server.listen()


if __name__ == "__main__":
    server = Server()
    server.listen()


