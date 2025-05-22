from ursina import *

class PauseMenu(Entity):
    def __init__(self, on_resume, on_restart, on_quit):
        super().__init__(enabled=False)
        self.panel = Entity(parent=camera.ui, model='quad', color=color.black66, scale=(0.8, 0.6), position=(0, 0))
        self.resume_btn = Button(text='Resume', position=(0, 0.2), scale=(0.3, 0.1), parent=self.panel, on_click=on_resume)
        self.restart_btn = Button(text='Restart', position=(0, 0), scale=(0.3, 0.1), parent=self.panel, on_click=on_restart)
        self.quit_btn = Button(text='Quit', position=(0, -0.2), scale=(0.3, 0.1), parent=self.panel, on_click=on_quit)
