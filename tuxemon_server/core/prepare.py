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
# core.prepare Prepares the game environment.
#
"""This module initializes the display and creates dictionaries of resources.
It contains all the static and dynamic variables used throughout the game such
as display resolution, scale, etc.
"""

import os
import shutil

from .components import config
from .platform import get_config_path


# Get the tuxemon base directory
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")) + os.sep

# Set up our config directory
CONFIG_PATH = get_config_path() + "/.tuxemon/"
try:
    os.makedirs(CONFIG_PATH)
except OSError:
    if not os.path.isdir(CONFIG_PATH):
        raise

# Create a copy of our default config if one does not exist in the home dir.
CONFIG_FILE_PATH = CONFIG_PATH + "tuxemon.cfg"
if not os.path.isfile(CONFIG_FILE_PATH):
    try:
        shutil.copyfile(BASEDIR + "tuxemon.cfg", CONFIG_FILE_PATH)
    except OSError:
        raise

# Read the "tuxemon.cfg" configuration file
CONFIG = config.Config(CONFIG_FILE_PATH)
HEADLESSCONFIG = config.HeadlessConfig(CONFIG_FILE_PATH)

# Set up the screen size and caption
SCREEN_SIZE = CONFIG.resolution
ORIGINAL_CAPTION = "Tuxemon"

# Set the native tile size so we know how much to scale our maps
TILE_SIZE = [16, 16]  # 1 tile = 16 pixels

# Set the status icon size so we know how much to scale our menu icons
ICON_SIZE = [7, 7]

# Native resolution is similar to the old gameboy resolution. This is
# used for scaling.
NATIVE_RESOLUTION = [240, 160]

# Set up the saves directory
try:
    os.makedirs(CONFIG_PATH + "saves/")
except OSError:
    if not os.path.isdir(CONFIG_PATH + "saves/"):
        raise
SAVE_PATH = CONFIG_PATH + "saves/slot"


def init():
    """The init function is used to initialize all dependent
    systems. This is primarily implemented to allow sphinx-apidoc
    to autogenerate documentation without initializing a PyGame
    window.

    :param None:

    :rtype: None
    :returns: None

    """

    # initialize any platform-specific workarounds before pygame
    from core import platform
    platform.init()

    # Create an instance of the player and list of NPCs
    from .components import player
    player1 = player.Player()

