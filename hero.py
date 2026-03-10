from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        """ Instance properties:
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
        Add armor to self.armors
        armor: Armor Object
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
        Return True or False depending on whether the hero is alive or not.
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
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

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
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

    print()

    shield = Armor("Shield", 50)
    force_field = Armor("Force Field", 20)
    hero.add_armor(shield)
    hero.add_armor(force_field)
    print(hero.defend())

    print()

    test_hero = Hero("Grace Hopper", 200)
    test_shield = Armor("Shield", 50)
    test_hero.add_armor(test_shield)
    test_hero.take_damage(50)
    print(test_hero.current_health)

    print(test_hero.is_alive())
    test_hero.take_damage(15000)
    print(test_hero.is_alive())

    print()

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)