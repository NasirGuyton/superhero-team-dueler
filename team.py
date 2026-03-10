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