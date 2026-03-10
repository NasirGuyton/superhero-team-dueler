from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        if self.current_health <= 0:
            return 0

        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        damage_taken = damage - self.defend()
        if damage_taken < 0:
            damage_taken = 0
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent_damage = opponent.attack()

            opponent.take_damage(self_damage)
            self.take_damage(opponent_damage)

        if self.is_alive() and not opponent.is_alive():
            self.add_kill(1)
            opponent.add_death(1)
            print(f"{self.name} won!")
        elif opponent.is_alive() and not self.is_alive():
            opponent.add_kill(1)
            self.add_death(1)
            print(f"{opponent.name} won!")
        elif not self.is_alive() and not opponent.is_alive():
            self.add_death(1)
            opponent.add_death(1)
            print("Draw")