class Weapon:
    def __init__(self, name, attack_power, crit_chance, rarity, ability, bonus_ability):
        self.name = name
        self.attack_power = attack_power # Bonus to damage
        self.crit_chance = crit_chance # Chance for Crit
        self.rarity = rarity 
        self.ability = ability # Strength or Dex?
        self.bonus_ability = bonus_ability # Bonus ability description

        # Getters
        def get_name(self):
            return self.name
        def get_attack_power(self):
            return self.attack_power
        def get_crit_chance(self):
            return self.crit_chance
        def get_rarity(self):
            return self.rarity
        def get_ability(self):
            return self.ability
        def get_bonus_ability(self):
            return self.bonus_ability

        # Setters
        def set_name(self, n):
            self.name = n
        def set_attack_power(self, a):
            self.attack_power = a
        def set_crit_chance(self, c):
            self.crit_chance = c
        def set_rarity(self, r):
            self.rarity = r
        def set_ability(Self, a):
            self.ability = a
        def set_bonus_ability(self, ba):
            self.bonus_ability = ba


# Dagger, attack_power = 4, 25%, common, dexterity, bleed - extra damage (50% chance of extra 1d4)
# Club, attack_power = 6, 10%, common, strength, Daze: -1 dexterity
# Sword, attack_power = 8, 12.5%, common, strength, Weaken: -1 defence
# Longbow, attack_power = 10, 17.5%, rare, dexterity, Pierce: 50% chance of extra 1d6 damage
# Greatsword, attack_power = 12, 15%, rare, strength, Topple: 50% chance of -2 defence
# Excalibur, attack_power = 16, 15%, legendary, strength, Virtue: Heal 5% each turn 

        
        