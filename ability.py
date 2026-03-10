import random


class Ability:
    def __init__(self, name, max_damage):
        """
        Initialize the values passed into this
        method as instance variables.
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """Return a random value between 0 and self.max_damage."""
        return random.randint(0, self.max_damage)


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())