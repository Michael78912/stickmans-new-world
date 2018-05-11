"""characters.py- a module of subclasses
each of these classes is a class of stickman from 
stickmanranger.
"""
from _internal import *
from character import Character

DEFAULT_STATS =(50, 0, 0, 0, 0)

class Swordsman(Character):
	image = PICS['characters']['swordsman']

	def __init__(self, player_num, stats=DEFAULT_STATS):
		Class.__init__(self, 'swordsman', stats)

class Angel(Class):
	image = PICS['characters']['angel']
	def __init__(self, player_num, stats=DEFAULT_STATS):
		Class.__init__(self, 'angel', stats)

class Archer(Class):
	image=PICS['characters']['archer']

	def __init__(self, player_num, stats=DEFAULT_STATS):
		Class.__init__(self, player_num, stats)

class Spearman(Class):
	image=PICS['characters']['spearman']

	def __init__(self, player_num, stats=DEFAULT_STATS):
		Class.__init__(self, player_num, stats)

class Wizard(Class):
	image=PICS['characters']['wizard']
	def __init__(self, player_num, stats=DEFAULT_STATS):
		Class.__init__(self, player_num, stats)

