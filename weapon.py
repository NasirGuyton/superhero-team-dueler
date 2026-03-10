import random
from ability import Ability


class Weapon(Ability):
    def attack(self):
        """
        Return a random value between one half of max_damage
        and full max_damage.
        """
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)


if __name__ == "__main__":
    weapon = Weapon("Sword of Testing", 80)
    print(weapon.name)
    print(weapon.attack())