import pygame

from gameObjects.SpriteGroups import SpriteGroup
from gameObjects.TankSprite import TankSprite


class Scene:
    def __init__(self, _gameObj, ):
        self.running = True
        self.dt = 0
        self.fps = 30
        self.gmo = _gameObj
        self.screen = _gameObj.screen

    def exit(self):
        pass

    def draw(self):
        pass

    def update(self, dt):
        pass

    def input(self, key):
        pass


class IntroScene(Scene):
    def __init__(self, _game_obj):
        super().__init__(_game_obj)


class GameScene(Scene):
    def __init__(self, _gameObj):
        super().__init__(_gameObj)
        self.running = True

        self.dt = 0
        self.fps = 30
        self.player_sprite = TankSprite(SpriteGroup(), sprites=None)
        self.dt = 0
        self.grid_size = 50

        self.grid = []

        for x in range(self.screen.get_width() // self.grid_size):
            row = []
            for y in range(self.screen.get_width() // self.grid_size):
                row.append((x,y))
            self.grid.append(row)

        # for debuging
        # print(self.grid)

    def exit(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

        # this is for development purposes
        # will show grid lines
        for x in range(0, self.screen.get_width(), self.grid_size):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (x, 0),
                             (x, self.screen.get_height())
                             )
        for y in range(0, self.screen.get_height(), self.grid_size):
            pygame.draw.line(self.screen, (255, 255, 255),
                             (0, y),
                             (self.screen.get_width(), y)
                             )
        pass

    def update(self, dt):
        pass

    def input(self, key):
        # print(f'key: {key},\nquit: {pygame.QUIT}')

        # if key == pygame.K_ESCAPE or event.key == pygame.QUIT:
        #     game.running = False

        pass
