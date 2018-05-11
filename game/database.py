"""this file contains basically all of the data that the game needs
it really has no code value, other than when it sorts the usable levels.
"""

import json as _json
import os.path

import pygame as _pg

#import class_ as _class_

#dictionary of color strings containing RGB values
COLOURS = {
    'green': (0, 128, 0),
    'blue': (0, 0, 128),
    'red': (128, 0, 0),
    'dark red': (255, 0, 0),
    'dark blue': (0, 0, 255),
    'dark green': (0, 255, 0),
    'black': (0, 0, 0),
    'aqua': (0, 255, 255),
    'white': (255, 255, 255),
    'teal': (0, 128, 128),
    'purple': (128, 128, 0),
    'dark purple': (255, 255, 0),
    'yellow': (255, 255, 0),
    'silver': (192, 192, 192),
    'gold': (192, 192, 96),
    'gray': (211, 211, 211),
}
open = lambda file: __builtins__.open(os.path.join('config', file))

SURFACE = _pg.display.set_mode((800, 600))

_DECODE = _json.JSONDecoder()

_USABLE  = _DECODE.decode(open('usable.json').read())
SETTINGS = _DECODE.decode(open('settings.json').read())
ALL = _DECODE.decode(open('data.json').read())
print(ALL)

ALL_LEVELS = {
	'village': _class_.Stage(position_on_map=(18, 589), all_screens=[None], boss_screen=None, )
}

ALL_SCREENS = [
	_class_.stage.Screen()
]

ALL_ENEMIES = [
    _class_.Blob((10, 1, 1, 1), COLOURS['green'],
    _class_.EnemyHead('smile', 'green'), 
    # need drops, and attack (not implemented)
    	)
]

ALL_WEAPONS = []

ALL_COMPOS = []

ALL_LEVELS = ALL_LEVELS[:]

MAIN_GAME_STATE = {
    'SETTINGS': SETTINGS,
    'GAME_DATA': {
    },
    'MAIN_DISPLAY_SURF': SURFACE,
}
