""" terrain_viewer.py - this version of terrain.py
is meant to be able to have a file type associated
with it.
"""
import sys
import pygame as pg
import os
from _internal import *
import request_email
import bugreport

surface_symbol = '*'
ground_symbol = '#'
water_symbol = '-'
air_symbol = '~'
sign_symbol = '^'
pit_symbol = '_'
top_water_symbol = '+'

# alpha values. can be overriden with headers. (see flat.smr-terrain)
air = 200
water = 100

def_air = (0, 0, 0, 200)
def_water = (0, 50, 200, 100)


def main():
    print('!!!!!!!!!!!!!', sys.argv)
    if len(sys.argv) == 1:
        test()

    elif len(sys.argv) == 2:
        list2d = read_file(sys.argv[1])
        surf = build_surface(list2d)

    else:
        list2d = read_file(sys.argv[1])
        surf = build_surface(list2d, sys.argv[2])

    draw(surf, sys.argv[1].split('.')[0])
    mainloop()


def read_file(file):
    print(file, '???????')
    terrain = open(file).read()
    global PICS, top_water
    PICS = gather_pics('data')
    top_water = PICS['Other']['top_water']
    main_dict = {
                'size': 10,
                'air': def_air, 
                'water': def_water
                 }
    if terrain.startswith('@'):
        print('howdy ho')
        # remove @ symbol
        header = terrain.split('\n')[0][1:]
        terrain = '\n'.join(terrain.split('\n')[1:])

        header = header.split('|')

        # remove all whitespace

        header = [part.strip().replace(' ', '').replace('\0', '')
                  .replace('\t', '').replace('\n', '').replace('\r', '') for part in header]

        for command in header:
            parts = command.split('=')
            if not parts[0] in ('air', 'water', 'size'):
                raise SyntaxError(
                    '%a is not a valid command for header' % parts[0])
            else:
                print('hullo')
                main_dict[parts[0]] = eval(parts[1])

    lines = []
    for line in terrain.split('\n'):
        if ';' in line:
            line = line.split(';')[0].strip()
        # dont append blank lines!
        if line != '':
            lines.append(line)

    terrain2dlist = []
    for line in lines:
        chars = []
        for char in line:
            chars.append(char)
        terrain2dlist.append(chars)

    main_dict['text'] = terrain2dlist

    return main_dict


def build_surface(text_dict, image='stone'):
    """
    builds the terrain image and returns it.
    also sets self.built_image to the surface.
    """
    self = object()
    pit_picture = PICS['Other']['pit']
    sign_picture = PICS['Other']['next']
    try:
        image1 = PICS['terrain_templates'][image]['1']
    except KeyError:
        # a command line argument has been set incorrectly
        # by the user. 
        image = 'stone'
        image1 = PICS['terrain_templates'][image]['1']

    image2 = PICS['terrain_templates'][image]['0']
    # the surface everything will be added to
    big_actual_picture = pg.surface.Surface((800, 400))
    # find the 2D list of the specified terrain
    template = text_dict
    self = Holder(**text_dict)
    pg.transform.scale(image1, (template['size'],) * 2)
    pg.transform.scale(image2, (template['size'],) * 2)
    if template['size'] is not None:
        self.size = template['size']

    text = template['text']
    air_picture = pg.surface.Surface((self.size,) * 2)
    air_picture.fill(template['air'])
    water_picture = pg.surface.Surface((self.size,) * 2)
    water_picture.fill(template['water'])
    top_water_picture = top_water
    _change_colour_surface(top_water_picture, *template['water'][:3])

    try:
        top_water_picture.set_alpha(template['water'][3])
    except IndexError:
        # no alpha has been set
        print('no alpha set')

    for line, index1 in zip(text, range(len(text))):
        for block, index2 in zip(line, range(len(line))):
            if block == ground_symbol:
                big_actual_picture.blit(image1, 
                    (index2 * self.size, index1 * self.size))
            elif block == surface_symbol:
                big_actual_picture.blit(image2, 
                    (index2 * self.size, index1 * self.size))
            elif block == air_symbol:
                big_actual_picture.blit(air_picture,
                    (index2 * self.size, index1 * self.size))
            elif block == water_symbol:
                big_actual_picture.blit(water_picture,
                    (index2 * self.size, index1 * self.size))
            elif block == pit_symbol:
                big_actual_picture.blit(air_picture,
                    (index2 * self.size, index1 * self.size))
                big_actual_picture.blit(pit_picture,
                    (index2 * self.size, index1 * self.size))
            elif block == top_water_symbol:
                big_actual_picture.blit(air_picture,
                    (index2 * self.size, index1 * self.size))
                big_actual_picture.blit(top_water_picture,
                    # sign is 30x30 pixels
                    (index2 * self.size, index1 * self.size))
            elif block == sign_symbol:
                big_actual_picture.blit(air_picture,
                    (index2 * self.size, index1 * self.size))
                big_actual_picture.blit(sign_picture,
                    # sign is 30x30 pixels
                    (index2 * self.size - 20, index1 * self.size - 10))
    self.built_image = big_actual_picture
    pg.transform.scale(big_actual_picture, (800, 400))
    return big_actual_picture


def _change_colour_surface(surface, r, g, b):
    """changes the colour of all parts of a 
    surface except for the transparent parts.
    """
    arr = pg.surfarray.pixels3d(surface)
    arr[:, :, 0] = r
    arr[:, :, 1] = g
    arr[:, :, 2] = b


class Holder:
    def __init__(self, **kwargs):
        for i, x in zip(kwargs, kwargs.values()):
            exec('self.{} = {}'.format(i, x))

def test():
    a = build_surface(read_file('terrains\\flat.smr-terrain'))
    surf = pg.display.set_mode((800, 400))
    surf.blit(a, (0, 0))

    while True:
        for event in pg.event.get():
            if event.type == 12:
                raise SystemExit
        pg.display.update()

def draw(surf, title=''):
    surface = pg.display.set_mode((800, 400))
    pg.display.set_caption(title)
    a = pg.transform.scale(PICS['terrain_templates']['dirt']['0'], (32, 32))
    pg.display.set_icon(a)
    surface.blit(surf, (0, 0))

def mainloop():
    while True:
        for event in pg.event.get():
            if event.type == 12:
                raise SystemExit
        pg.display.update()
try:
    if len(sys.argv) > 2:
        print(sys.argv, len(sys.argv), len(sys.argv) > 2)
        sys.argv[1] = os.path.join(os.getcwd(), sys.argv[1])
        print(sys.argv)

    os.chdir(os.path.dirname(sys.executable))

    request_email.main()
    main()

except Exception as e:
    bugreport.mainwithmessage('Terrain Viewer', e, 'this is probably an error on koens computer, as no one else  has probably downloaded it')