#!/usr/bin/python

import tuxemon_server.core.game.player

def move_player(event):
    client_id = event["cuuid"]
    direction = event["parameters"]
    return core.game.player.move(client_id, direction)
