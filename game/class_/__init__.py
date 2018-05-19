"""
__init__.py- this is the only module that will 
be loaded on calling 'import class_', so i thought
it would be good to bundle everything in here.
it is expected that this will only be called
from .., so this should be fine
"""

try:
    from .screen import Screen, PeacefulScreen
    from .backgroundimage import BackGroundImage
    from .stage import Stage
    from .inventory import InventoryHandler
    from .enemy_head import EnemyHead
    from .my_rect import MyRect
    from .smr_error import SMRError
    from .terrain import Terrain
    from .weapon import *
    from .characters import *
    from .enemies import *
    import class_.enemies
    import class_.klass

except:
    from inventory import InventoryHandler
    from screen import Screen, PeacefulScreen
    from backgroundimage import BackGroundImage
    from stage import Stage
    from enemy_head import EnemyHead
    from my_rect import MyRect
    from smr_error import SMRError
    from terrain import Terrain
    from weapon import *
    from characters import *
    from enemies import *
    import enemies
    import klass

HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII = 0
print(dir())
