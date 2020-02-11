from pygame.sprite import Sprite


class Base(Sprite):
    def __init__(self, groups, _game_obj):
        super().__init__(*groups)
        self.image = None
        self.rect = None
        self.game = _game_obj

    def update(self, *args):
        pass

    def input(self, key):
        pass
