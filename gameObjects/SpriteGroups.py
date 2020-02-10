from pygame.sprite import Group


class SpriteGroup(Group):

    def __init__(self, *sprites):
        super().__init__(*sprites)

    def input(self, key):
        pass
