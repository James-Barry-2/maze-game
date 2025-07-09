<<<<<<< HEAD
from game_map import GameMap
from character import Character
import random

items = ["Healing Potion", "Greater Healing Potion", "Old Gloves", "Goblet", 
         "Old Map", "Shield", "Bejeweled Crown", "Sword", "Longbow", "Club", "Staff", "Excalibur"]


def trigger_encounter(character):
    print("You encountered something")
    random_item = random.sample(items, 1)[0]
    print(random_item)
    character.add_inventory(random_item)



def enter_room(character, game_map, room_position):
    room_type = game_map.get_tile(room_position[0], room_position[1])
    if room_type == '?':
        trigger_encounter(character)
    if room_type == 'M':
        begin_combat(character, Character(name='Monster', level=1, health=20, max_health=20, position=room_position, inventory=[], strength=3, dexerity=2, defence=1, weapon='club', attack_power=6))
    if room_type == 'X':
        print("You've been here before...")
    if room_type == 'H':
        print("fuck")
    return



def take_turn(character, game_map):
    print("What would you like to do? [move, use item, status]")
    action = input("Enter your action: ").strip().lower()
    if action == "move":
        make_a_move(character, game_map)
    if action == "use item":
        use_an_item(character)
    if action == "status":
        character.status()



def make_a_move(character, game_map):
    print("What direction would you like to move? [up, down, right, left]")
    direction = input("Enter your move: ").strip().lower()
    if direction in ["up", "down", "left", "right"]:
        room_pos = character.position
        if direction == "up":
            room_pos = (room_pos[0], room_pos[1] - 1)
        elif direction == "down":
            room_pos = (room_pos[0], room_pos[1] + 1)
        elif direction == "right":
            room_pos = (room_pos[0] + 1, room_pos[1])
        elif direction == "left":
            room_pos = (room_pos[0] - 1, room_pos[1])
        enter_room(character, game_map, room_position=room_pos)
        character.move(direction, game_map)
        game_map.print_map(character.position[0], character.position[1], game_map.world_map, False)


def use_an_item(character):
    available_items = character.get_inventory()
    print("Your available items are: ")
    for i in range(len(available_items)):
        print(available_items[i])
    if len(available_items) == 0:
        print("You have no items to use")
        return
    else:
        print("What item would you like to use?")
        chosen_item = input("Enter desired item: ").strip().lower()
        if chosen_item == "healing potion":
            character.heal(25)
            character.remove_inventory("Healing Potion")
        elif chosen_item == "greater healing potion":
            character.heal(50)
            character.remove_inventory("Greater Healing Potion")
        elif chosen_item == "shield":
            character.set_defence(character.get_defence() + 2)
            character.remove_inventory("Shield")
        elif chosen_item == "sword":
            print("You equip a sword")
            character.set_weapon("sword")
        elif chosen_item == "greatsword":
            print("You equip a greatsword")
            character.set_weapon("greatsword")
        elif chosen_item == "excalibur":
            print("You equip the legendary Excalibur!")
            character.set_weapon("excalibur")
        elif chosen_item == "longbow":
            print("You equip a longbow")
            character.set_weapon("longbow")
        elif chosen_item == "staff":
            print("You equip a staff")
            character.set_weapon("staff")
        elif chosen_item == "club":
            print("You equip a club")
            character.set_weapon("club")
        else:
            print("Item does nothing")
        

def attack(character, enemy):
    print(f"{character.get_name()} attacks {enemy.get_name()}")

    attack_power = character.get_attack_power()

    critical_hit_chance = attack_power * 0.2
    roll = random.randint(0, 100)
    if roll <= critical_hit_chance:
        crit_multiplier = 2
    else: crit_multiplier = 1

    damage = ((random.randint(0, attack_power) + character.get_strength()) * crit_multiplier) - enemy.get_defence()
    if damage < 0:
        damage = 0
    enemy.set_health(enemy.get_health() - damage)
    print(f"{enemy.get_name()} takes {damage} damage!")

def take_combat_turn(character, enemy):
    print(f"{character.get_name()}'s turn!")
    print("What would you like to do? [attack, use item]")
    action = input("Enter your action: ").strip().lower()
    if action == 'attack':
        attack(character, enemy)
    elif action == 'use item':
        use_an_item(character)


def begin_combat(character, enemy):
    print(f"You are now in combat with {enemy.get_name()}")
    print("----------------------")

    if character.get_dexerity() >= enemy.get_dexerity():
        print(f"{character.get_name()} goes first!")
        turn_order = [character, enemy]
    else:
        print(f"{enemy.get_name()} goes first!")
        turn_order = [enemy, character]

    while character.get_health() > 0 and enemy.get_health() > 0:
        attacker = turn_order[0]
        defender = turn_order[1]

        print(f"{character.get_name()} Health: {character.get_health()} / {character.get_max_health()}")
        #print(f"{enemy.get_name()} Health: {enemy.get_health()} / {enemy.get_max_health()}")

        if attacker == character:
            take_combat_turn(character, enemy)
        else:
            attack(enemy, character)

        turn_order.reverse()
        print("----------------------")

        if character.get_health() <= 0:
            print(f"{character.get_name()} is dead!")
            return False
        if enemy.get_health() <= 0:
            print(f"{enemy.get_name()} is dead!")
            return True


        
=======
from game_map import GameMap
from character import Character
import random

items = ["Healing Potion", "Greater Healing Potion", "Old Gloves", "Goblet", 
         "Old Map", "Shield", "Bejeweled Crown", "Sword", "Longbow", "Club", "Staff", "Excalibur"]


def trigger_encounter(character):
    print("You encountered something")
    random_item = random.sample(items, 1)
    print(random_item)
    character.add_inventory(random_item)



def enter_room(character, game_map, room_position):
    room_type = game_map.get_tile(room_position[0], room_position[1])
    if room_type == '?':
        trigger_encounter(character)
    if room_type == 'M':
        begin_combat(character, Character(name='Monster', level=1, health=20, max_health=20, position=room_position, inventory=[], strength=3, dexerity=2, defence=1, weapon='club', attack_power=6))
    if room_type == 'X':
        print("You've been here before...")
    if room_type == 'H':
        print("fuck")
    return



def take_turn(character, game_map):
    print("What would you like to do? [move, use item, status]")
    action = input("Enter your action: ").strip().lower()
    if action == "move":
        make_a_move(character, game_map)
    if action == "use item":
        use_an_item(character)
    if action == "status":
        character.status()



def make_a_move(character, game_map):
    print("What direction would you like to move? [up, down, right, left]")
    direction = input("Enter your move: ").strip().lower()
    if direction in ["up", "down", "left", "right"]:
        room_pos = character.position
        if direction == "up":
            room_pos = (room_pos[0], room_pos[1] - 1)
        elif direction == "down":
            room_pos = (room_pos[0], room_pos[1] + 1)
        elif direction == "right":
            room_pos = (room_pos[0] + 1, room_pos[1])
        elif direction == "left":
            room_pos = (room_pos[0] - 1, room_pos[1])
        enter_room(character, game_map, room_position=room_pos)
        character.move(direction, game_map)
        game_map.print_map(character.position[0], character.position[1], game_map.world_map, False)


def use_an_item(character):
    available_items = character.get_inventory()
    print("Your available items are: ")
    for i in range(len(available_items)):
        print(available_items[i])
    if len(available_items) == 0:
        print("You have no items to use")
        return
    else:
        print("What item would you like to use?")
        chosen_item = input("Enter desired item: ").strip().lower()
        if chosen_item == "healing potion":
            character.heal(25)
            character.remove_inventory("Healing Potion")
        elif chosen_item == "greater healing potion":
            character.heal(50)
            character.remove_inventory("Greater Healing Potion")
        elif chosen_item == "shield":
            character.set_defence(2)
            character.remove_inventory("Shield")
        elif chosen_item == "sword":
            print("You equip a sword")
            character.set_weapon("sword")
        elif chosen_item == "greatsword":
            print("You equip a greatsword")
            character.set_weapon("greatsword")
        elif chosen_item == "excalibur":
            print("You equip the legendary excalibur!")
            character.set_weapon("excalibur")
        elif chosen_item == "longbow":
            print("You equip a longbow")
            character.set_weapon("longbow")
        elif chosen_item == "staff":
            print("You equip a staff")
            character.set_weapon("staff")
        elif chosen_item == "club":
            print("You equip a club")
            character.set_weapon("club")
        else:
            print("Item does nothing")
        

def attack(character, enemy):
    print(f"{character.get_name()} attacks {enemy.get_name()}")

    attack_power = character.get_attack_power()

    # Determine critical hit chance
    critical_hit_chance = attack_power * 0.2
    # Does Crit happen?
    roll = random.randint(0, 100)
    if roll <= critical_hit_chance:
        crit_multiplier = 2
    else: crit_multiplier = 1

    damage = ((random.randint(0, attack_power) + character.get_strength()) * crit_multiplier) - enemy.get_defence()
    if damage < 0:
        damage = 0
    enemy.set_health(enemy.get_health() - damage)
    print(f"{enemy.get_name()} takes {damage} damage!")

def take_combat_turn(character, enemy):
    print(f"{character.get_name()}'s turn!")
    print("What would you like to do? [attack, use item]")
    action = input("Enter your action: ").strip().lower()
    if action == 'attack':
        attack(character, enemy)
    elif action == 'use item':
        use_an_item(character)


def begin_combat(character, enemy):
    print(f"You are now in combat with {enemy.get_name()}")
    print("----------------------")

    if character.get_dexerity() >= enemy.get_dexerity():
        print(f"{character.get_name()} goes first!")
        turn_order = [character, enemy]
    else:
        print(f"{enemy.get_name()} goes first!")
        turn_order = [enemy, character]

    while character.get_health() > 0 and enemy.get_health() > 0:
        attacker = turn_order[0]
        defender = turn_order[1]

        print(f"{character.get_name()} Health: {character.get_health()} / {character.get_max_health()}")
        #print(f"{enemy.get_name()} Health: {enemy.get_health()} / {enemy.get_max_health()}")

        if attacker == character:
            take_combat_turn(character, enemy)
        else:
            attack(enemy, character)

        turn_order.reverse()
        print("----------------------")

        if character.get_health() <= 0:
            print(f"{character.get_name()} is dead!")
            return False
        if enemy.get_health() <= 0:
            print(f"{enemy.get_name()} is dead!")
            return True


        
>>>>>>> 2b0734f8ce33ed860adc69e4354616b534041f9d
