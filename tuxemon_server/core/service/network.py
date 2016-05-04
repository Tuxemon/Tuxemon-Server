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
# core.service.network Networking related module
#

from neteria.tools import _Middleware
from tuxemon_server.core import controllers

class Middleware(_Middleware):
    def event_legal(self, cuuid, euuid, event_data):
        # We need to do authentication checks here for every request.

        # Ensure the request has an event_type
        if "event_type" not in event_data:
            print("Error: Event type not found in event data: %s" % str(event_data))
            return False

        # Check to see if we have a function for the requested event type.
        event_type = event_data["event_type"]
        if event_type not in controllers.all_functions.keys():
            print("Error: Event type '%s' not supported" % str(event_type))
            return False

        return True

    def event_execute(self, cuuid, euuid, event_data):
        # Here we need to dynamically execute the appropriate method in
        # controllers.
        event_type = event_data["event_type"]
        if event_type in controllers.all_functions.keys():
            controllers.all_functions[event_type](event_data)
