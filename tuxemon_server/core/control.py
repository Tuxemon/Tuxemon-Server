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

from neteria.server import NeteriaServer
from tuxemon_server.core.service.network import Middleware
from tuxemon_server.core.tools import Clock
from tuxemon_server.core.game.cli import CommandLine

# DEBUG
#import time

class Control(object):
    def __init__(self):
        self.clock = Clock()
        self.exit = False
        self.server = NeteriaServer(Middleware())
        self.cli = CommandLine(self)

    def main_loop(self):
        dt = self.clock.tick()
        if self.exit:
            self.done = True

    def start(self):
        self.server.listen()
        while not self.exit:
            self.main_loop()


"""Example
class HeadlessControl(object):
    def __init__(self):
        self.done = False

        self.clock = time.clock()
        self.fps = 60.0
        self.current_time = 0.0

        # TODO: move out to state manager
        self.package = "core.states"
        self.state_dict = dict()
        self._state_stack = list()

        self.server = networking.TuxemonServer(self)
        # self.server_thread = threading.Thread(target=self.server)
        # self.server_thread.start()
        self.server.server.listen()

        # Set up our game's configuration from the prepare module.
        self.config = prepare.HEADLESSCONFIG

        # Set up the command line. This provides a full python shell for
        # troubleshooting. You can view and manipulate any variables in
        # the game.
        self.exit = False  # Allow exit from the CLI
        if self.config.cli:
            self.cli = cli.CommandLine(self)

    def main_loop(self):
        # Get the amount of time that has passed since the last frame.
        # self.time_passed_seconds = time.clock() - self.clock
        # self.server.update()

        if self.exit:
            self.done = True

    def main(self):
        while not self.exit:
            self.main_loop()
"""
