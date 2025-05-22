# File: core/physics_engine.py
from ursina import *

def check_collisions(plane, objects):
    for obj in objects:
        if plane.intersects(obj).hit:
            plane.on_collision(obj)
            break