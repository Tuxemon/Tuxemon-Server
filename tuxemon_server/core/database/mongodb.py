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
# core.components.db Database handling module.
#
#

import logging
from pymongo import MongoClient

from tuxemon_server.core import database
from tuxemon_server.core import prepare

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class MongoDBDatabase(database.AbstractDatabase):

    def configure(self, host, port, username, password, ssl, db_name):
        self.client = MongoClient(host, ssl=ssl, port=port)
        self.db = self.client[db_name]
        if username:
            self.db.authenticate(username, password)


    def aggregate(self, collection_name, pipeline):
        """Aggregate for colleciton_name using aggregation operations

        Args:
            collection_name: The collection name from which you want to aggregate results
            pipeline: Array of dictionary of pipeline operations you want to perform to get the result
        """
        return getattr(self.db, collection_name).aggregate(pipeline, allowDiskUse=True)


    def find_all(self, colleciton_name, query=None):
        """Find all entries from a collection using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        return getattr(self.db, colleciton_name).find(query).batch_size(1000)


    def find_one(self, colleciton_name, query=None):
        """Find one and only one entry from a collection using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        return getattr(self.db, colleciton_name).find_one(query)


    def count(self, collection_name, query=None):
        return getattr(self.db, collection_name).find(query).count()


    def drop(self, colleciton_name):
        return self.db.drop_collection(colleciton_name)


    def save(self, collection_name, data, db=None):
        if db:
            return getattr(self.client[db], collection_name).save(data)
        else:
            return getattr(self.db, collection_name).save(data)

