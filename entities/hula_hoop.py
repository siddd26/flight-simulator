# File: entities/hula_hoop.py
from ursina import *

class HulaHoop(Entity):
    def __init__(self, position=(0, 2, 0)):
        super().__init__(
            model='torus',
            color=color.orange,
            scale=(3, 3, 0.3),
            position=position,
            collider='mesh'
        )
        self.rotation_speed = 60

    def update(self):
        self.rotation_y += time.dt * self.rotation_speed