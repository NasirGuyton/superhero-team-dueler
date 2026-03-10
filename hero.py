import random


class Hero:
    def __init__(self, name, starting_health=100):
        """
        Instance properties:
            name: String
            starting_health: Integer
            current_health: Integer
        """
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """
        Current Hero will fight the opponent hero passed in.
        Randomly chooses a winner and prints the result.
        """
        winner = random.choice([self, opponent])
        loser = opponent if winner == self else self

        print(f"{winner.name} defeats {loser.name}!")


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    print()

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)