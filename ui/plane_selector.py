from ursina import *
import os

class PlaneSelector(Entity):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.panel = Entity(parent=camera.ui, model='quad', color=color.black66, scale=(0.6, 0.6), position=(0, 0))

        self.title = Text(text='Select Your Plane', parent=self.panel, y=0.25, scale=2, origin=(0, 0), color=color.white)

        self.buttons = []
        plane_dir = 'assets/models/planes/'
        plane_names = [f[:-4].replace('_', ' ').title() for f in os.listdir(plane_dir) if f.endswith('.obj')]

        button_spacing = 0.3
        start_pos_x = -(len(plane_names) - 1) * button_spacing / 2

        for i, name in enumerate(plane_names[:3]): # Limit to the first 3 planes for the example layout
            x_pos = start_pos_x + i * button_spacing
            btn = Button(parent=self.panel, scale=(0.2, 0.2), position=(x_pos, -0.1))
            btn.on_click = Func(self.select_plane, name)
            self.buttons.append(btn)
            Text(text=name, parent=btn, y=-0.6, origin=(0, 0), color=color.white, scale=2)

    def select_plane(self, name):
        self.disable()
        self.callback(name)