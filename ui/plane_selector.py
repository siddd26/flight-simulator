from ursina import *
import os

class PlaneSelector(Entity):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.panel = Entity(parent=camera.ui, model='quad', color=color.black66, scale=(0.6, 0.6), position=(0, 0))

        self.title = Text(text='Select Your Plane', parent=self.panel, y=0.25, scale=2, origin=(0, 0), color=color.white)

        self.buttons = []
        plane_dir = 'models/planes/'
        plane_names = [f[:-4] for f in os.listdir(plane_dir) if f.endswith('.obj')]

        for i, name in enumerate(plane_names):
            btn = Button(text=name, parent=self.panel, scale=(0.4, 0.1), position=(0, 0.1 - i*0.15))
            btn.on_click = Func(self.select_plane, name)
            self.buttons.append(btn)

    def select_plane(self, name):
        self.disable()
        self.callback(name)
