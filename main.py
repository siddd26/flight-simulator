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
from ui.main_menu import MainMenu
import random, json, os

app = Ursina()
window.title = '3D Flight Simulator'
window.borderless = False
window.fullscreen = False
window.color = color.cyan

# Load sounds and other assets
preload_assets()

# Global variables
score = 0
high_scores = []
save_file = 'leaderboard.json'
score_text = Text(text=f'Score: {score}', position=(-0.85, 0.45), scale=2, color=color.white)
game_state = 'menu' # 'menu', 'gameplay', 'game_over'
player_plane = None
input_controller = None
entities = []
progression_manager = None

paused = False
pause_menu = None
music_on = True
game_over_screen = None
weather_notice = None
background_music = Audio('assets/sounds/plane.wav', autoplay=True, loop=True)

# Load leaderboard
if os.path.exists(save_file):
    with open(save_file, 'r') as f:
        high_scores = json.load(f)
# Game State Management
def pause_game():
    global paused, game_state
    paused = not paused
    if paused:
        application.pause()
        pause_menu.enable()
    else:
        application.resume()
        pause_menu.disable()

def restart_game():
    global score, score_text, entities, player_plane, game_state
    destroy(player_plane)
    for e in entities:
        destroy(e)
    entities.clear()
    
    score = 0
    score_text.text = f'Score: {score}' # Reset score text
    
    # Recreate a basic plane for simplicity
    player_plane = PlayerPlane(model_name='default_plane')
    game_state = 'gameplay'

def quit_game():
    application.quit()



# Game Over Screen

def show_game_over():
    global game_over_screen
    game_over_screen = Entity(parent=camera.ui)
    Text(text='Game Over', scale=3, position=(0, 0.2), origin=(0, 0), parent=game_over_screen)
    Text(text=f'Final Score: {score}', scale=2, position=(0, 0.05), origin=(0, 0), parent=game_over_screen)
    Button(text='Restart', scale=(0.2, 0.05), position=(0, -0.1), parent=game_over_screen, on_click=lambda: [destroy(game_over_screen), restart_game()])
    Button(text='Quit', scale=(0.2, 0.05), position=(0, -0.2), parent=game_over_screen, on_click=quit_game)

    # Save score
    high_scores.append(score)
    high_scores.sort(reverse=True)
    high_scores[:] = high_scores[:5]  # Keep top 5
    with open(save_file, 'w') as f:
        json.dump(high_scores, f)

    y_offset = -0.35
    for i, s in enumerate(high_scores):
        Text(text=f'{i+1}. {s}', scale=1.5, position=(0, y_offset), origin=(0, 0), parent=game_over_screen)
        y_offset -= 0.07

def start_game():
    global player_plane, input_controller, game_state
    main_menu.disable()
    plane_selector.disable() # Ensure plane selector is also disabled
    game_state = 'gameplay'
    player_plane = PlayerPlane(model_name='default_plane') # Start with default plane
    input_controller = InputController(player_plane)

    Entity(model='plane', texture='textures/environment/ground.png', scale=(100,1,100), collider='box', y=-1)
    Sky(texture='textures/environment/skybox.png')

    for _ in range(15):
        building = Building(position=(random.uniform(-10, 10), 0, random.uniform(10, 100)))
        entities.append(building)

# Main update loop
def update():
    global score, game_state
    if game_state != 'gameplay' or not player_plane:
        return

    input_controller.update()
    player_plane.update() # Assuming PlayerPlane has an update method

    for entity in entities[:]:
        # Basic forward movement for entities for simplicity
        entity.position -= player_plane.forward * time.dt * 10 

        if isinstance(entity, Coin) and player_plane.intersects(entity).hit: # Check for coin collision
            score += 1
            score_text.text = f'Score: {score}' # Update score display
            destroy(entity)
            entities.remove(entity)

        elif isinstance(entity, Building) and player_plane.intersects(entity).hit:
            camera.shake(duration=.5, magnitude=.5)
            invoke(show_game_over, delay=0.2)
            application.pause()
            return
        
        # Basic despawn for entities that pass
        if entity.position.z < player_plane.position.z - 20:
             destroy(entity)
             entities.remove(entity)

# Initialize main menu
main_menu = MainMenu()
main_menu.find_button_by_text('Start').on_click = start_game
main_menu.find_button_by_text('Choose Plane').on_click = lambda: [main_menu.disable(), plane_selector.enable()]
main_menu.find_button_by_text('Quit').on_click = quit_game

# Initialize plane selector (disabled initially)
plane_selector = PlaneSelector(callback=start_game)
plane_selector.disable()

app.run()