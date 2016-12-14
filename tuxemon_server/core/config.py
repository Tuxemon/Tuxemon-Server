#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tuxemon
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
# core.config Configuration parser.
#
#
try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Config(object):
    """Handles loading of the configuration file.

    """
    def __init__(self, config_path="server.cfg"):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        print(config_path)

        # Game configuration
        self.starting_map = self.config.get("game", "starting_map")
        self.starting_position = [int(self.config.get("game", "starting_position_x")),
                                  int(self.config.get("game", "starting_position_y"))]
        self.cli = int(self.config.get("game", "cli_enabled"))

        # Logging configuration
        self.debug_logging = self.config.get("logging", "debug_logging")
        self.debug_level = str(self.config.get("logging", "debug_level")).lower()
        self.loggers = self.config.get("logging", "loggers")
        self.loggers = self.loggers.replace(" ", "").split(",")

        # Transport Configuration
        self.transport = self.config.get("transport", "provider")
        self.listen_address = self.config.get("transport", "listen_address")
        self.listen_port = self.config.get("transport", "listen_port")

        # Parser Configuration
        self.parser = self.config.get("parser", "provider")

        # User Auth Configuration
        self.auth = self.config.get("auth", "provider")

        # Database Configuration
        self.db_provider = self.config.get("database", "provider")
        self.db_user = self.config.get("database", "username")
        self.db_pass = self.config.get("database", "password")
        self.db_port = self.config.getint("database", "port")
        self.db_host = self.config.get("database", "host")
        self.db_ssl = self.config.getboolean("database", "ssl")
        self.db_database = self.config.get("database", "database")
