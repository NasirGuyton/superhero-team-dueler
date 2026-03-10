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
            deaths: Integer
            kills: Integer
        """
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        """Add weapon to self.abilities."""
        self.abilities.append(weapon)

    def add_armor(self, armor):
        """Add armor to self.armors."""
        self.armors.append(armor)

    def attack(self):
        """
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

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
        damage_taken = damage - self.defend()

        if damage_taken < 0:
            damage_taken = 0

        self.current_health -= damage_taken

    def is_alive(self):
        """
        Return True if hero is alive, otherwise False.
        """
        return self.current_health > 0

    def add_kill(self, num_kills):
        """Update self.kills by num_kills amount."""
        self.kills += num_kills

    def add_death(self, num_deaths):
        """Update deaths with num_deaths."""
        self.deaths += num_deaths

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


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.add_ability(Ability("Super Strength", 200))
    hero1.add_weapon(Weapon("Lasso of Truth", 100))
    hero1.add_armor(Armor("Amazon Shield", 50))

    hero2.add_ability(Ability("Magic Blast", 150))
    hero2.add_weapon(Weapon("Wizard Staff", 80))
    hero2.add_armor(Armor("Magic Barrier", 40))

    hero1.fight(hero2)

    print(hero1.name, "Kills:", hero1.kills, "Deaths:", hero1.deaths)
    print(hero2.name, "Kills:", hero2.kills, "Deaths:", hero2.deaths)