import sys
import os

class PATHERROR(Exception):
    def __init__(self, path):
        super().__init__()
        self.path = path
    def __str__(self):
        return self.path + ' does not exist'

BASE_DIR = ''

default_x = 500
default_y = 500
default_bg_color = (0, 0, 0)
default_fps = 27


if sys.argv[1] == '-B':
    chosen_dir = BASE_DIR + '\\' + sys.argv[2]
else:
    chosen_dir = sys.argv[1]

if not os.access(os.path.split(chosen_dir)[0], os.F_OK) or not chosen_dir.endswith('.py'):
    raise PATHERROR(chosen_dir)

with open(chosen_dir, 'w') as file:
    sys.stdout = file
    print('import pygame')
    print('pygame.init()')
    print()
    print('width, height = ' + str(default_x) + ', '+str(default_y))
    print()
    print('screen = pygame.display.set_mode((width, height))')
    print()
    print('clock = pygame.time.Clock()')
    print()
    print('#define own variables')
    print()
    print('def redraw()')
    print('    screen.fill('+str(default_bg_color)+')')
    print('    #define own draw-actions')
    print('    pyame.display.update()')
    print()
    print('while 1:')
    print('    for event in pygame.event.get():')
    print('        if event.type == pygame.QUIT:')
    print('            break')
    print()
    print('    clock.tick('+str(default_fps)+')')
    print()
    print('    #define own actions')
    print()
    print('    redraw()')
    print()
    print('pygame.quit()')
    sys.stdout = sys.__stdout__
