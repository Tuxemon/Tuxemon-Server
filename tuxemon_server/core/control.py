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

from tuxemon_server.core.tools import Clock
from tuxemon_server.core.network import network
from tuxemon_server.core.game.cli import CommandLine

# DEBUG
#import time

class Control(object):
    def __init__(self):
        self.clock = Clock()
        self.server = network.Server()
        self.exit = False
        self.cli = CommandLine(self)

    def main_loop(self):
        dt = self.clock.tick()
        if self.exit:
            self.done = True

    def start(self):
        self.server.listen()
        while not self.exit:
            self.main_loop()


