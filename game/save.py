"""
save.py- create game save for stickmans new world.

data: read_file
takes no arguments, and returns a data structure (dict)
of the save, without any of the classes.

write_file(data)
data must be a dict (or dict-like file like IniFile)
and write it to $HOME/.stickman_new_world/save/.smr-save on linux
or %USERPROFILE%/.stickman_new_world/save/.smr-save on windows

convert(data)
convert data from dict of strings to
actual stickman's new world data.
"""

import inifile
import os
import encrypt


def read_file():
	game_state = {}
	data_text, time = encrypt.decrypt()
	data_file = os.path.join(
	    os.getenv('TMP'), '.save.ini') if os.name == 'nt' else '/tmp/.save.cfg'

	with open(data_file, 'w') as open_file:
		open_file.write(data_text)

	ini_file = inifile.IniFile(data_file)
	print(ini_file.to_dict())

	keys = ini_file.keys()
	values = ini_file.values()

	for key, value in zip(keys, values):
		if '.' in key:
			# value is in a category
			klass, prop = key.split('.')
			print(klass, prop)
			try:
				game_state[klass]
			except KeyError:
				game_state[klass] = {}

			game_state[klass][prop] = prop

		else:
			game_state[key] = value
	print(game_state == ini_file.to_dict())

if __name__ == '__main__':
	encrypt.encrypt(open('misc\\shello.ini').read())
	print(read_file())
