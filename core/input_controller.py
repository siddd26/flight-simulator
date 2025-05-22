# File: core/input_controller.py
from ursina import *

class InputController:
    def __init__(self, plane):
        self.plane = plane

    def update(self):
        self.plane.update()