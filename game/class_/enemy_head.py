import pygame

try:
    from _internal import PICS, COLOURS
except ImportError:
    from ._internal import PICS, COLOURS

DEF_SIZE = 1

class EnemyHead:
    def __init__(self, type_str, colour, size=DEF_SIZE):
        print(size)
        img = PICS['heads'][type_str][colour].copy()
        self.head = pygame.transform.scale(img, (size * 10, size * 10))
        print({100: COLOURS[' '.join(('light', colour))]})
        change_alpha_to_colour(self.head, {100: COLOURS['light ' + colour]})
        self.name = colour + '_' + type_str
        self.pretty_name = ' '.join((colour, type_str)).title()

def change_alpha_to_colour(surf, alpha_to_colour):
    #print(alpha_to_colour)
    for alpha_value, colour in zip(alpha_to_colour.keys(),
                                   alpha_to_colour.values()):
        alpha = pygame.surfarray.pixels_alpha(surf)
        colours = pygame.surfarray.pixels3d(surf)
        #print(alpha)
        for i, index1 in zip(alpha, range(len(alpha))):
            for val, index in zip(i, range(len(i))):
                if val == alpha_value:
                    colours[index1][index] = colour
                    alpha[index1][index] = 255

def main():
    import pygame
    image = pygame.image.load('happy.png')
    pygame.image.save(image, 'purplehappy.png')


import pprint
pprint.pprint(PICS)


if __name__ == '__main__':
    s = EnemyHead('happy', 'green')
    print(vars(s))
    import pygame
    pygame.image.save(s.head, 'C:\\Users\\Michael\\Desktop\\head.png')
    a = pygame.display.set_mode((1000, 1000))
    a.fill(COLOURS['white'])
    s.head.set_alpha(100)
    #change_alpha_to_colour(s.head, {100: (255, 0, 0)})
    a.blit(s.head, (0,0))
    pygame.display.update()
    while True:
        for i in pygame.event.get():
            if i.type == 12:
                raise SystemExit

