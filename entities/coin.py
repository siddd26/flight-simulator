# File: entities/coin.py
from ursina import *

coin_audio = Audio('assets/sounds/coin.wav', autoplay=False)

class Coin(Entity):
    def __init__(self, position):
        super().__init__(model='circle', color=color.yellow, scale=0.5, position=position, collider='box')
        self.name = 'coin'

    def on_trigger_enter(self, other):
        if isinstance(other, Entity) and 'plane' in other.name:
            coin_audio.play()
            destroy(self)