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
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)


if __name__ == "__main__":
    from hero import Hero

    team = Team("Justice League")

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Batman")
    hero3 = Hero("Superman")

    team.add_hero(hero1)
    team.add_hero(hero2)
    team.add_hero(hero3)

    print("All heroes:")
    team.view_all_heroes()

    print("\nRemoving Batman...")
    team.remove_hero("Batman")

    print("\nAll heroes after removal:")
    team.view_all_heroes()