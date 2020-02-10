from pygame.sprite import Sprite


class Base(Sprite):
    def __init__(self, *groups, sprites):
        super().__init__(*groups)
        self.sprites = sprites
        self.image = None
        self.rect = None

    def update(self, *args):
        pass

    def input(self, key):
        pass
