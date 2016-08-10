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
# core.components.database.sqlite Sqlite3 database provider module.
#
#

import logging
import sqlite3

from tuxemon_server.core import database

# Create a logger for optional handling of debug messages.
logger = logging.getLogger(__name__)
logger.debug("%s successfully imported" % __name__)

class SqliteDatabase(database.AbstractDatabase):

    def configure(self, host, port, username, password, ssl, db_name):
        self._conn = sqlite3.connect(db_name)

    def _ensure_tables(self):
        c = self._conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS {} (id integer, username string, password string, email string)"
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query.format("accounts"))


    def find_all(self, table_name, field, value):
        """Find all entries from a table using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        self._ensure_tables()
        c = self._conn.cursor()
        query = "SELECT * FROM {} WHERE {}=?".format(table_name, field)
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query, value)

        return c.fetchall()


    def find_one(self, table_name, field, value):
        """Find one and only one entry from a table using a query

        Args:
            colleciton_name: The collection from which you want to get all entries from
            query: A dictionary of keys and value for the query
        """
        self._ensure_tables()
        c = self._conn.cursor()
        query = "SELECT * FROM {} WHERE {}=? LIMIT 1".format(table_name, field)
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query, value)

        return c.fetchone()


    def count(self, table_name, field, value):
        self._ensure_tables()
        c = self._conn.cursor()
        query = "SELECT count(*) FROM {} WHERE {}=?".format(table_name, field)
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query, value)

        return c.fetchone()


    def drop(self, table_name):
        self._ensure_tables()
        c = self._conn.cursor()
        query = "DROP TABLE {}".format(table_name)
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query)

        return c.fetchone()


    def save(self, table_name, data):
        self._ensure_tables()
        c = self._conn.cursor()
        values = "?, " * len(data)
        query = "INSERT INTO {} VALUES({})".format(table_name, values)
        logger.debug("Executing SQL query: {}".format(query))
        c.execute(query, data.values())

        return c.fetchone()
