# File: core/game_manager.py
from ursina import *
from entities.coin import Coin
from entities.hula_hoop import HulaHoop
from entities.building import Building
import random

class GameManager:
    def __init__(self, player):
        self.player = player
        self.entities = []
        self.score = 0

    def update(self):
        for entity in self.entities:
            entity.enabled = distance(self.player.position, entity.position) < 50

        # Simplified collision handling (will be handled in main.py for now)
        # for coin in self.coins:
        #     if coin.enabled and coin.intersects(self.player).hit:
        #         coin.disable()
        #         Audio('assets/coin_pickup.ogg').play()
        #         self.score += 10

        # for hoop in self.hoops:
        #     if hoop.enabled and hoop.intersects(self.player).hit:
        #         hoop.disable()
        #         Audio('assets/hoop_pass.ogg').play()
        #         self.score += 25
            if coin.enabled and coin.intersects(self.player).hit:
                coin.disable()
                Audio('assets/coin_pickup.ogg').play()
                self.score += 10

        for hoop in self.hoops:
            if hoop.enabled and hoop.intersects(self.player).hit:
                hoop.disable()
                Audio('assets/hoop_pass.ogg').play()
                self.score += 25