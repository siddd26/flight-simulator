# File: core/asset_loader.py
import os
from ursina import *

def load_models_from_folder(folder_path):
    models = []
    for file in os.listdir(folder_path):
        if file.endswith(".obj"):
            models.append(os.path.join(folder_path, file))
    return models


def preload_assets():
    for sound in ['assets/sounds/crash.wav', 'assets/sounds/coin.wav']:
        Audio(sound, autoplay=False)