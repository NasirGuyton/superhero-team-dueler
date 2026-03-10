import random


class Armor:
    def __init__(self, name, max_block):
        """
        Instantiate instance properties.
            name: String
            max_block: Integer
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return a random value between 0 and self.max_block."""
        return random.randint(0, self.max_block)


if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())