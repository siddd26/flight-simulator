# File: entities/plane.py
from ursina import *
import os

class PlayerPlane(Entity):
    def __init__(self, model_name='default_plane'):
        super().__init__()
        model_path = f'models/planes/{model_name}.obj'
        self.model = model_path if os.path.exists(model_path) else 'cube'
        self.texture = 'white_cube'
        self.scale = 0.75
        self.collider = BoxCollider(self, center=Vec3(0,0,0), size=Vec3(1,0.5,2))
        self.speed = 5

    def update(self):
        self.y += held_keys['w'] * time.dt * self.speed
        self.y -= held_keys['s'] * time.dt * self.speed
        self.x -= held_keys['a'] * time.dt * self.speed
        self.x += held_keys['d'] * time.dt * self.speed
        self.rotation_z = clamp(self.rotation_z - held_keys['a']*2 + held_keys['d']*2, -20, 20)
        self.rotation_x = clamp(self.rotation_x + held_keys['s']*2 - held_keys['w']*2, -10, 10)
        self.z += time.dt * self.speed * 1.5
