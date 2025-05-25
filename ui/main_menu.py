from ursina import *

class MainMenu(Entity):
    def __init__(self):
        super().__init__()
        self.panel = Entity(parent=camera.ui, model='quad', color=color.black66, scale=(0.8, 0.8), position=(0, 0))

        self.title = Text(text='Flight Simulator', parent=self.panel, y=0.35, scale=3, origin=(0, 0), color=color.white)

        # Button layout
        button_scale = (0.3, 0.15)
        button_spacing = 0.05

        # Row 1
        self.weather_button = Button(text='Weather\n(coming soon)', parent=self.panel, scale=button_scale, position=(-button_scale[0]/2 - button_spacing/2, button_scale[1]/2 + button_spacing/2))
        self.info_button = Button(text='Info', parent=self.panel, scale=button_scale, position=(button_scale[0]/2 + button_spacing/2, button_scale[1]/2 + button_spacing/2))

        # Row 2
        self.choose_plane_button = Button(text='Choose Plane', parent=self.panel, scale=button_scale, position=(-button_scale[0]/2 - button_spacing/2, -button_scale[1]/2 - button_spacing/2))
        self.start_button = Button(text='Start', parent=self.panel, scale=button_scale, position=(button_scale[0]/2 + button_spacing/2, -button_scale[1]/2 - button_spacing/2))