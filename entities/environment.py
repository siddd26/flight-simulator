# File: entities/environment.py
from ursina import *

class Environment(Entity):
    def __init__(self):
        super().__init__()

        # Sky
        self.sky = Sky()

        # Ground
        self.ground = Entity(
            model='plane',
            texture='white_cube',
            texture_scale=(100, 100),
            scale=(200, 1, 200),
            color=color.green,
            collider='box',
            position=(0, 0, 0)
        )
