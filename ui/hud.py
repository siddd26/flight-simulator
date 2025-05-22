# File: ui/hud.py
from ursina import *

class HUD(Entity):
    def __init__(self):
        super().__init__()
        self.score_text = Text(text='Score: 0', position=(-0.85, 0.45), scale=1.5, color=color.white)

    def update_score(self, score):
        self.score_text.text = f'Score: {score}'