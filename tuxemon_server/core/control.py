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
# control.py Controls server functions
#

from tuxemon_server.core import prepare
from tuxemon_server.core import transport
from tuxemon_server.core import parser
from tuxemon_server.core import database
from tuxemon_server.core import auth
from tuxemon_server.core.game import Game
from tuxemon_server.core.game.cli import CommandLine
from tuxemon_server.core.tools import Clock

# DEBUG
#import time

class Control(object):
    def __init__(self):
        prepare.init()
        self.configure()
        self.clock = Clock()
        self.exit = False
        self.game = Game()
        self.cli = CommandLine(self)

    def configure(self):
        # Setup our database, parser, and transport layers.
        config = prepare.CONFIG
        db = database.configure(config.db_provider,
                                config.db_host,
                                config.db_port,
                                config.db_user,
                                config.db_pass,
                                config.db_ssl,
                                config.db_database)
        auth.configure(config.auth)
        parse = parser.configure(config.parser)
        trans = transport.configure(config.transport,
                                    parse,
                                    config.listen_address,
                                    config.listen_port)

        self.transport = trans

    def main_loop(self):
        dt = self.clock.tick()
        if self.exit:
            self.done = True

    def start(self):
        self.transport.listen()
        while not self.exit:
            self.main_loop()


