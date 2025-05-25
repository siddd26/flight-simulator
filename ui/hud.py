# File: ui/hud.py
from ursina import *

class HUD(Entity):
    def __init__(self):
        super().__init__()
        # Coin icon
        self.coin_icon = Entity(
            parent=camera.ui,
            model='assets/models/items/coin.obj',  # Assuming this is the path to your coin model
            color=color.gold,
            scale=0.05,
            position=(-0.88, 0.45) # Position the icon slightly to the left of the text
        )
        self.score_text = Text(text='0', position=(-0.85, 0.45), scale=1.5, color=color.white)

    def update_score(self, score):
        self.score_text.text = str(score)