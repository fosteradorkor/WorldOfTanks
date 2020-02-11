import pygame
from pygame.time import Clock

from gameObjects.Scene import Scene, IntroScene, GameScene
from gameObjects.SpriteGroups import SpriteGroup
from gameObjects.TankSprite import TankSprite

pygame.init()


class Game():
    STATE_INTRO = 0
    STATE_GAME = 1
    STATE_PAUSE = 2

    def __init__(self, _screen):
        self.screen = _screen
        self.state = Game.STATE_GAME
        self.running = True
        self.clock = Clock()

        self._scenes = [
            IntroScene(self),
            GameScene(self)
        ]

    def draw(self):
        self.get_scene().draw()
        pass

    def update(self):
        pass

    def input(self):
        events = pygame.event.get()
        for event in events:
            # complete quit
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # game.input(event.key)
                pass

    def get_scene(self):
        '''
        gets the current scene of the game
        :return: Scene object
        '''
        return self._scenes[self.state]

    def exit(self):
        '''
        basic cleanup
        :return:
        '''
        pass

    def run(self):
        while self.running:
            self.clock.tick(self.get_scene().fps)

            self.input()
            self.update()
            self.draw()
            pygame.display.update()

        self.exit()


if __name__ == '__main__':
    size = (600, 600)
    screen = pygame.display.set_mode(size)

    game = Game(screen)
    game.run()

