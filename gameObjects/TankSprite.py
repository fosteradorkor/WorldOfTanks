from gameObjects.Base import Base


class TankSprite(Base):
    def __init__(self, *groups, sprites):
        super().__init__(*groups, sprites=sprites)

    def update(self, **kwargs):
        super(TankSprite, self).update(kwargs)
        pass
