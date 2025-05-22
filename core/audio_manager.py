from ursina import *

class AudioManager:
    def __init__(self):
        self.music = Audio('assets/music.ogg', loop=True, autoplay=False)
        self.plane_sound = Audio('assets/plane.ogg', loop=True, autoplay=False)
        self.muted = False

    def toggle_music(self):
        self.muted = not self.muted
        self.music.volume = 0 if self.muted else 1

    def play_background_music(self):
        self.music.play()

    def play_plane_sound(self):
        self.plane_sound.play()
