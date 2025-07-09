from constants import color

class Character:
    def __init__(self, name, level, health, max_health, position, inventory, strength, 
        dexerity, defence, attack_power, weapon):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.level = level
        self.position = position
        self.inventory = []
        self.strength = strength
        self.dexerity = dexerity
        self.defence = defence
        self.weapon = weapon
        self.attack_power = attack_power

    # Getters
    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_max_health(self):
        return self.max_health
    def get_level(self):
        return self.level
    def get_position(self):
        return self.position
    def get_inventory(self):
        return self.inventory
    def get_defence(self):
        return self.defence
    def get_strength(self):
        return self.strength
    def get_dexerity(self):
        return self.dexerity
    def get_weapon(self):
        return self.weapon
    def get_attack_power(self):
        return self.attack_power
    
    # Setters
    def set_name(self, new_name):
        self.name = new_name
    def set_health(self, new_health):
        if new_health > self.max_health:
            self.health = self.max_health
        else:
            self.health = new_health
    def set_max_health(self, new_max_health):
        self.max_health = new_max_health
    def set_level(self, new_level):
        self.level = new_level
    def set_positoin(self, new_position):
        self.position = new_position
    def set_defence(self, amount):
        self.defence = self.defence + amount
    def set_strength(self, amount):
        self.strength = amount
    def set_weapon(self, weapon):
        self.weapon = weapon
        if weapon == 'sword':
            self.set_attack_power(self, 10)
        elif weapon == 'club':
            self.set_attack_power(self, 6)
        elif weapon == 'longbow':
            self.set_attack_power(self, 8)
        elif weapon == 'dagger':
            self.set_attack_power(self, 4)
        elif weapon == 'staff':
            self.set_attack_power(self, 8)
        elif weapon == 'greatsword':
            self.set_attack_power(self, 12)
        elif weapon == 'excalibur':
            self.set_attack_power(self, 16)
    def set_dexerity(self, amount):
        self.dexerity = amount
    def set_attack_power(self, new_attack_power):
        self.attack_power = new_attack_power

    # Custom Functions
    def add_inventory(self, item):
        self.inventory.append(item)
    def remove_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f"ERROR: {item} not found in inventory.")
    def heal(self, amount):
        self.health =+ amount
        if self.health > self.max_health:
            self.health = self.max_health
    

    def status(self):
        print("Giving status rn")
        print(f"Name: {self.name}")
        print(f"Health: {self.health} / {self.max_health}")
        print(f"Inventory: {self.inventory}")
        
    
    def move(self, direction, game_map):
        x, y = self.position
        if direction == 'up':
            if y > 0:
                game_map.set_tile(self.position[0], self.position[1], (color.GREEN + 'X' + color.END))
                self.position = (x, y - 1)
            else:
                print("You can't move up, you're at the edge of the map.")
        elif direction == 'down':
            if y < game_map.height - 1:
                game_map.set_tile(self.position[0], self.position[1], (color.GREEN + 'X' + color.END))
                self.position = (x, y + 1)
            else:
                print("You can't move down, you're at the edge of the map.")
        elif direction == 'left':
            if x > 0:
                game_map.set_tile(self.position[0], self.position[1], (color.GREEN + 'X' + color.END))
                self.position = (x - 1, y)
            else:
                print("You can't move left, you're at the edge of the map.")
        elif direction == 'right':
            if x < game_map.width - 1:
                game_map.set_tile(self.position[0], self.position[1], (color.GREEN + 'X' + color.END))
                self.position = (x + 1, y)
            else:
                print("You can't move right, you're at the edge of the map.")
        
        game_map.set_tile(self.position[0], self.position[1], 'H')


        
            
        
        