import random


class Team:
    def __init__(self, name):
        """Initialize your team with its team name and an empty list of heroes."""
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """Add Hero object to self.heroes."""
        self.heroes.append(hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        found_hero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
                break

        if not found_hero:
            return 0

    def view_all_heroes(self):
        """Prints out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        """Print team statistics."""
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        """Reset all heroes health to starting_health."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        """Battle each team against each other."""
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)

        for hero in other_team.heroes:
            if hero.is_alive():
                living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            living_heroes = [hero for hero in self.heroes if hero.is_alive()]
            living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]


if __name__ == "__main__":
    from hero import Hero
    from ability import Ability
    from armor import Armor
    from weapon import Weapon

    team_one = Team("Justice League")
    team_two = Team("Wizards")

    hero1 = Hero("Wonder Woman")
    hero1.add_ability(Ability("Super Strength", 200))
    hero1.add_weapon(Weapon("Lasso of Truth", 100))
    hero1.add_armor(Armor("Bracelets", 40))

    hero2 = Hero("Batman")
    hero2.add_ability(Ability("Martial Arts", 120))
    hero2.add_weapon(Weapon("Batarang", 80))
    hero2.add_armor(Armor("Suit Armor", 30))

    hero3 = Hero("Dumbledore")
    hero3.add_ability(Ability("Magic Blast", 180))
    hero3.add_weapon(Weapon("Elder Wand", 110))
    hero3.add_armor(Armor("Magic Shield", 35))

    hero4 = Hero("Gandalf")
    hero4.add_ability(Ability("Fire Spell", 160))
    hero4.add_weapon(Weapon("Staff Strike", 90))
    hero4.add_armor(Armor("Wizard Cloak", 25))

    team_one.add_hero(hero1)
    team_one.add_hero(hero2)

    team_two.add_hero(hero3)
    team_two.add_hero(hero4)

    team_one.attack(team_two)

    print("\nTeam One Stats:")
    team_one.stats()

    print("\nTeam Two Stats:")
    team_two.stats()