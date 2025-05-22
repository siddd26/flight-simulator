# File: main.py
from ursina import *
from ui.plane_selector import PlaneSelector
from entities.plane import PlayerPlane
from entities.coin import Coin
from entities.hula_hoop import HulaHoop
from entities.building import Building
from core.asset_loader import preload_assets
from core.physics_engine import check_collisions
from core.input_controller import InputController
from core.progression_manager import ProgressionManager
import random

app = Ursina()
window.title = '3D Flight Simulator'
window.borderless = False
window.fullscreen = False
window.color = color.cyan

# Load sounds and other assets
preload_assets()

# Global variables
score = 0
score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2, color=color.white)

player_plane = None
input_controller = None
entities = []
progression_manager = None

paused = False
pause_menu = None
music_on = True
background_music = Audio('assets/sounds/plane.wav', autoplay=True, loop=True)

# UI buttons
def toggle_music():
    global music_on
    music_on = not music_on
    background_music.volume = 1 if music_on else 0

def pause_game():
    global paused
    paused = not paused
    if paused:
        application.pause()
        pause_menu.enable()
    else:
        application.resume()
        pause_menu.disable()

def restart_game():
    destroy(player_plane)
    for e in entities:
        destroy(e)
    entities.clear()
    global score, score_text
    score = 0
    score_text.text = f'Score: {score}'
    start_game_with_plane(player_plane.model.split('/')[-1][:-4])

def quit_game():
    application.quit()

pause_menu = Entity(enabled=False, parent=camera.ui)
Button(text='Resume', scale=(0.2, 0.05), position=(0, 0.1), parent=pause_menu, on_click=pause_game)
Button(text='Restart', scale=(0.2, 0.05), position=(0, 0), parent=pause_menu, on_click=restart_game)
Button(text='Toggle Music', scale=(0.2, 0.05), position=(0, -0.1), parent=pause_menu, on_click=toggle_music)
Button(text='Quit', scale=(0.2, 0.05), position=(0, -0.2), parent=pause_menu, on_click=quit_game)

# Plane selection callback
def start_game_with_plane(model_name):
    global player_plane, input_controller, entities, progression_manager

    player_plane = PlayerPlane(model_name=model_name)
    input_controller = InputController(player_plane)
    progression_manager = ProgressionManager(player_plane, entities)

    Entity(model='plane', texture='textures/environment/ground.png', scale=(100,1,100), collider='box', y=-1)
    Sky(texture='textures/environment/skybox.png')

    for _ in range(10):
        coin = Coin(position=(random.uniform(-10, 10), 1, random.uniform(10, 100)))
        entities.append(coin)

    for _ in range(5):
        hoop = HulaHoop(position=(random.uniform(-10, 10), 3, random.uniform(10, 100)))
        entities.append(hoop)

    for _ in range(15):
        building = Building(position=(random.uniform(-10, 10), 0, random.uniform(10, 100)))
        entities.append(building)

# Main update loop
def update():
    global score

    if held_keys['escape']:
        pause_game()

    if paused or not player_plane:
        return

    input_controller.update()
    check_collisions(player_plane, entities)
    progression_manager.update()

    for entity in entities[:]:
        if isinstance(entity, Coin) and player_plane.intersects(entity).hit:
            score += 1
            score_text.text = f'Score: {score}'
            destroy(entity)
            entities.remove(entity)

# Instructions
instructions = Text(text='WASD to Fly | ESC to Pause | Collect Coins | Avoid Buildings', position=(0, 0.45), scale=1.5, origin=(0,0), color=color.azure)

# Start menu
plane_selector = PlaneSelector(callback=start_game_with_plane)

app.run()