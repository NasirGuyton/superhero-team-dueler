from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        """
        Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        """
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """Add weapon to self.abilities."""
        self.abilities.append(weapon)

    def attack(self):
        """
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        """
        Add armor to self.armors.
        """
        self.armors.append(armor)

    def defend(self):
        """
        Calculate the total block amount from all armor blocks.
        return: total_block:Int
        """
        if self.current_health <= 0:
            return 0

        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        """
        Updates self.current_health to reflect the damage minus the defense.
        """
        defense = self.defend()
        damage_taken = damage - defense

        if damage_taken < 0:
            damage_taken = 0

        self.current_health -= damage_taken

    def is_alive(self):
        """
        Return True if hero is alive, otherwise False.
        """
        return self.current_health > 0

    def fight(self, opponent):
        """
        Current Hero will take turns fighting the opponent hero passed in.
        """
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            opponent_damage = opponent.attack()

            opponent.take_damage(self_damage)
            self.take_damage(opponent_damage)

            if self.is_alive() and not opponent.is_alive():
                print(f"{self.name} won!")
                return
            elif opponent.is_alive() and not self.is_alive():
                print(f"{opponent.name} won!")
                return
            elif not self.is_alive() and not opponent.is_alive():
                print("Draw")
                return


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())