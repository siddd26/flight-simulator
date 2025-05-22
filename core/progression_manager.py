# File: core/progression_manager.py
from ursina import *
from entities.building import Building
from entities.coin import Coin
from entities.hula_hoop import HulaHoop
import random

class ProgressionManager:
    def __init__(self, player, scene):
        self.player = player
        self.scene = scene
        self.spawn_distance = 50
        self.spawn_interval = 20
        self.last_spawn_z = 0

    def update(self):
        if self.player.z > self.last_spawn_z + self.spawn_interval:
            for _ in range(5):
                x = random.uniform(-10, 10)
                z = self.player.z + self.spawn_distance + random.uniform(0, 10)
                entity_type = random.choice(['building', 'coin', 'hoop'])
                if entity_type == 'building':
                    b = Building(position=(x, 0, z))
                    self.scene.append(b)
                elif entity_type == 'coin':
                    c = Coin(position=(x, random.uniform(1, 3), z))
                    self.scene.append(c)
                else:
                    h = HulaHoop(position=(x, random.uniform(2, 5), z))
                    self.scene.append(h)
            self.last_spawn_z = self.player.z
