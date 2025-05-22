# File: entities/building.py
from ursina import *
import random

class Building(Entity):
    def __init__(self, position):
        height = random.uniform(2, 6)
        super().__init__(model='cube', color=color.gray, scale=(2, height, 2), position=(position[0], height/2, position[2]), collider='box')
        self.name = 'building'
