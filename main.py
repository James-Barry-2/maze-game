import random
from game_map import GameMap
from character import Character
from utils import take_turn

size = 3
map = GameMap(height=size, width=size)
guy = Character(name='Guy', level = 1, health=40, max_health=40, position=(0, 0), inventory=["Healing Potion"], strength = 4, dexerity = 4, defence = 3, weapon='sword', attack_power=10)

map.generate_map()
map.print_map(guy.position[0], guy.position[1], map.world_map, False)



while True:
    take_turn(guy, map)
    if guy.position == (size - 1, size - 1):
        print("You did it. GAME OVER")
        break

# Need to do:
# - Add a way to exit the game
# - More combat options
#   - New monster types
#   - Spells
# - New map shapes
# - Arrow keys to move
# - Add see whole map functionality to 'Old Map'
# - Levels