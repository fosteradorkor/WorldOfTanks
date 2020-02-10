import pygame

from gameObjects.SpriteGroups import SpriteGroup
from gameObjects.TankSprite import TankSprite

size = (800, 600)


class Game:
    def __init__(self, _size):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()

        self.dt = 0
        self.fps = 30
        self.screen = pygame.display.set_mode(_size)
        self.player_sprite = TankSprite(SpriteGroup(), sprites=None)
        self.dt = 0
        self.ucount = 0

    def exit(self):
        pass

    def draw(self):
        pass

    def update(self):
        self.dt = self.clock.tick(self.fps)

        self.ucount += 1
        if self.ucount > 30:
            self.ucount = 0
        print(f'update : {self.ucount}')



        pass

    def input(self, key):
        if key == pygame.K_ESCAPE or event.key == pygame.QUIT:
            game.running = False

        pass


if __name__ == '__main__':

    game = Game(size)

    while game.running:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.KEYDOWN:
                game.input(event.key)

        # update
        game.update()

        game.draw()

        pygame.display.update()

    game.exit()
