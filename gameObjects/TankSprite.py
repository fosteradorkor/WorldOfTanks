import os

import pygame

from gameObjects.Base import Base


class Tank:
    classA = 'A'
    classB = 'B'
    classC = 'C'
    classD = 'D'


class TankSprite(Base):
    def __init__(self, _game_obj, *groups, _tank_class=Tank.classA):
        super().__init__(groups, _game_obj)
        self.grid_pos = (0, 0)
        self.generate_sprite(_tank_class)
        # print()

    def update(self, **kwargs):
        super(TankSprite, self).update(kwargs)
        pass

    def generate_sprite(self, _tank_class):
        # generating tank image
        gun = pygame.image.load(
            os.path.join(os.getcwd(), 'assets', 'sprites', f'Weapon_Color_{_tank_class}', 'Gun_01.png')) \
            .convert_alpha()
        hull = pygame.image.load(
            os.path.join(os.getcwd(), 'assets', 'sprites', f'Hulls_Color_{_tank_class}', 'Hull_01', '0.png')) \
            .convert_alpha()
        hull.blit(gun, (hull.get_width() // 2 - gun.get_width() // 2, 0))

        self.image = hull

        # scale down image with respect to longer side
        ratio = self.game.grid_size / max(self.image.get_rect().width, self.image.get_rect().height)
        self.image = pygame.transform.scale(self.image, (
            int(self.image.get_rect().width * ratio), int(self.image.get_rect().height * ratio)))

        self.rect = self.image.get_rect()

        # center game object into individual cells
        self.rect.center = (
            (self.grid_pos[0] + self.game.grid_size) // 2, (self.grid_pos[1] + self.game.grid_size) // 2,)

        pass
