"""
_internal.py - a VERY messy module that i 
kind of hate myself for making, but a lot of my 
files in the class_ library rely on it 
(if i could remove it, I would) :(
"""

import os
import sys

import pygame as pg
from pygame.locals import *

import random

print(sys.executable, 'HOWDY HO')

BACKWARDS = 'backwards'
FORWARDS = 'forwards'
DIR = '.'

__author__ = 'NOT Michael Gill'
__version__ = '0.0'

VALID_ENEMY_HEADS = ['smile', 'frown', 'triangle']
col = {
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


def gather_pics(dir='.'):

    dictionary = {}

    for item in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, item)):
            dictionary[item] = gather_pics(os.path.join(dir, item))

        elif item.split(".")[-1] in ('png', 'jpg'):
            dictionary[item.split('.')[0]] = pg.image.load(
                os.path.join(dir, item))

    return dictionary


#PICS = _gather_pics(os.path.join(os.path.dirname(sys.executable), 'data'))
#PICS = _gather_pics('data')
TDIR = os.path.join(DIR, 'terrains')
"""characters.py- a module of subclasses
each of these classes is a class of stickman from 
stickmanranger.
"""

DEFAULT_STATS = (50, 0, 0, 0, 0)


def _Box(size, colour, pos, surface, alpha=None, image=None) -> tuple:
    """
    return a square rectangle, surface pair
    uses MyRect
    """
    print(pos)
    new_surf = pg.surface.Surface(size)
    new_surf.fill(colour)

    if alpha is not None:
        new_surf.set_alpha(alpha)

    surface.blit(new_surf, pos)

    if image is not None:
        surface.blit(image, pos)

    return MyRect(new_surf.get_rect(topleft=pos)), new_surf
