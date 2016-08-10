
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
# core.tools Tools for Tuxemon Server
#

import time
import base64
import uuid
import hashlib

try:
    import bcrypt
except ImportError:
    bcrypt = None

class Clock(object):
    """Clock is a generic clock for keeping track of the time passed between "frames".
    """
    def __init__(self):
        self.previous = time.time()

    def tick(self):
        current = time.time()
        dt = current - self.previous
        self.previous = current
        return dt

def generate_id():
    """Generates a 32 character long unique id.
    """
    return uuid.uuid4()

def hash_password(password):
    """Generates a salted hash of the given password. If bcrypt is installed it will
    use its method of salting and hashing passwords for storage.
    """
    if bcrypt:
        return _bcrypt_hash_password(password)
    return _sha_salt_hash_password(password)

def _bcrypt_hash_password(password):
    """Hashes and salts a given string using bcrypt.
    """
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password, salt)

    return password_hash

def _sha_salt_hash_password(password, salt=None):
    """Hashes and salts a given string using sha512 and uuid salts.
    """
    if not salt:
        salt = generate_id().hex
    password_hash = hashlib.sha512(password + salt).hexdigest()

    # Prepend the salt to the password hash so we can use it for verification.
    # The salt is the first 32 characters of the string for uuid4.
    password_hash = salt + password_hash

    return password_hash

def verify_password(password, stored_hash):
    """Verifies the has of the given password and compares it against a stored hash.
    If bcrypt is installed it will use its method of salting and hashing passwords for storage.
    """
    if bcrypt:
        return _bcrypt_verify_password(password, stored_hash)
    return _sha_salt_verify_password(password, stored_hash)

def _bcrypt_verify_password(password, stored_hash):
    """Verifies a password against a stored salted hash using bcrypt.
    """
    return stored_hash == bcrypt.hashpw(password, stored_hash)

def _sha_salt_verify_password(password, stored_hash):
    """Verifies a password against a stored salted hash using sha512 and uuid salts.
    """
    # Grab the salt from the stored hash. The salt is the first 32 characters
    # for uuid4.
    salt = stored_hash[:32]
    password_hash = _sha_salt_hash_password(password, salt)

    return stored_hash == password_hash
