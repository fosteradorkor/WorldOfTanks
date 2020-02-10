import pygame

from gameObjects.TankSprite import TankSprite


class Game:
    def __init__(self, size):
        pygame.init()
        self.player_sprite = TankSprite()
        self.running = False
        self.dt = 0
        self.fps = 30
        self.screen = pygame.display.set_mode(size)

    def exit(self):
        pass

    def update(self):
        pass

    def input(self, key):
        if key == pygame.K_ESCAPE or event.key == pygame.QUIT:
            game.running = False

        pass


if __name__ == '__main__':
    game = Game()

    while game.running:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.KEYDOWN:
                game.input(event.key)

        # update
        game.update()
