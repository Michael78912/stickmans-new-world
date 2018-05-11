"""
dicts.py
this module holds functions and data that deal
with large dictionaries, which this game uses a lot
of 
GetPics-return a dictionary containing 
string keys and pygame image equivelants.
COLOURS: a dictionary containing string keys
and RGB tuple values."""
import os
from pygame.image import load
from database import *

__author__ = 'Michael Gill'
__version__ = '0.0'


def gather_pics(dir='.'):

    dictionary = {}

    print(dir)

    for item in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, item)):
            print(dir, item)
            dictionary[item] = gather_pics(os.path.join(dir, item))

        elif item.split(".")[-1] in ('png', 'jpg'):
            if dir in ('heads', 'attacks',) + tuple(ALL['all_weapons'].values()):
                # heads, attacks, and weapons should be of each colour
                for key, value in zip(COLOURS.keys(), COLOURS.values()):
                    dictionary['_'.join((key, item))] = change_colour_surface(
                        load(os.path.join(dir, item)), *value)

            else:
                print(item)
                dictionary[item.split('.')[0]] = load(os.path.join(dir, item))

    return dictionary


def change_colour_surface(surface, r, g, b):
    """changes the colour of all parts of a 
    surface except for the transparent parts.
    """
    arr = pg.surfarray.pixels3d(surface)
    arr[:, :, 0] = r
    arr[:, :, 1] = g
    arr[:, :, 2] = b



if __name__ == '__main__':
    dict = gather_pics('data')
    print(dict)
