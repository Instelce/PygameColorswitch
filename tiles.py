import pygame

from settings import *
from support import import_folder


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('purple')
        self.rect = self.image.get_rect(topleft=(x, y))

    def update():
        pass


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()


class Coin(AnimatedTile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y, path)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.rect = self.image.get_rect(center=(center_x, center_y))


class Spike(Tile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.image.fill('gray')
        self.rect = self.image.get_rect(center=(center_x, center_y))


class Key(Tile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y)
        center_x = x + int(size / 2)
        center_y = y + int(size / 2)
        self.image.fill('#ecaa6b')
        self.rect = self.image.get_rect(center=(center_x, center_y))


class Goal(Tile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y)
        self.image.fill('brown')
        self.rect = self.image.get_rect(topleft=(x, y))
