# File: core/game_manager.py
from ursina import *
from entities.coin import Coin
from entities.hula_hoop import HulaHoop
from entities.building import Building
import random

class GameManager:
    def __init__(self, player):
        self.player = player
        self.coins = []
        self.hoops = []
        self.buildings = []
        self.score = 0

        self.spawn_entities()

    def spawn_entities(self):
        for i in range(20):
            x, y, z = random.randint(-100, 100), 1, random.randint(-100, 100)
            self.coins.append(Coin(position=(x, y, z)))

        for i in range(10):
            x, y, z = random.randint(-100, 100), 2, random.randint(-100, 100)
            self.hoops.append(HulaHoop(position=(x, y, z)))

        for i in range(30):
            x, y, z = random.randint(-100, 100), 0, random.randint(-100, 100)
            self.buildings.append(Building(position=(x, y, z)))

    def update(self):
        for entity in self.coins + self.hoops + self.buildings:
            entity.enabled = distance(self.player.position, entity.position) < 50

        for coin in self.coins:
            if coin.enabled and coin.intersects(self.player).hit:
                coin.disable()
                Audio('assets/coin_pickup.ogg').play()
                self.score += 10

        for hoop in self.hoops:
            if hoop.enabled and hoop.intersects(self.player).hit:
                hoop.disable()
                Audio('assets/hoop_pass.ogg').play()
                self.score += 25