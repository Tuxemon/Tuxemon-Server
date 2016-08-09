#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (C) 2014, William Edwards <shadowapex@gmail.com>,
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
# core.components.config Configuration parser.
#
#
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Config(object):
    """Handles loading of the configuration file for the primary game and map editor.

    """
    def __init__(self, file="server.cfg"):
        self.config = configparser.ConfigParser()
        self.config.read(file)

        self.starting_map = self.config.get("game", "starting_map")
        self.starting_position = [int(self.config.get("game", "starting_position_x")),
                                  int(self.config.get("game", "starting_position_y"))]
        self.cli = int(self.config.get("game", "cli_enabled"))

        self.debug_logging = self.config.get("logging", "debug_logging")
        self.debug_level = str(self.config.get("logging", "debug_level")).lower()
        self.loggers = self.config.get("logging", "loggers")
        self.loggers = self.loggers.replace(" ", "").split(",")

        self.listen_address = self.config.get("server", "listen_address")
        self.listen_port = self.config.get("server", "listen_port")

        self.mongodb_user = self.config.get("mongodb", "username")
        self.mongodb_pass = self.config.get("mongodb", "password")
        self.mongodb_port = self.config.getint("mongodb", "port")
        self.mongodb_host = self.config.get("mongodb", "host")
        self.mongodb_ssl = self.config.getboolean("mongodb", "ssl")
        self.mongodb_database = self.config.get("mongodb", "database")


