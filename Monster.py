import random

# Monster constants
MIN_MONSTER_HEALTH = 40
MAX_MONSTER_HEALTH = 80
MIN_MONSTER_STRENGTH = 20
MAX_MONSTER_STRENGTH = 40


class Monster:
    """
    Represents a monster in a dungeon room.
    """

    def __init__(self, name):
        self._name = name
        self._health = random.randint(MIN_MONSTER_HEALTH, MAX_MONSTER_HEALTH)
        self._strength = random.randint(MIN_MONSTER_STRENGTH, MAX_MONSTER_STRENGTH)

    @property
    def name(self):
        # Returns the monster's name.
        return self._name

    @property
    def health(self):
        # Returns the monster's current health.
        return self._health

    @property
    def strength(self):
        # Returns the monster's strength.
        return self._strength

    def attack(self):
        # Returns the monster's strength as attack damage.
        return self._strength

    def take_damage(self, damage):
        # Reduces health by the given damage amount. Health cannot go below 0.
        self._health -= damage
        if self._health < 0:
            self._health = 0
        print(
            f"{self._name} took {damage} damage "
            f"and now has {self._health} health."
        )

    def is_alive(self):
        # Returns True if the monster's health is above 0.
        return self._health > 0

    def get_status(self):
        # Returns a string describing the monster's current status.
        return (
            f"Monster: {self._name}, Health: {self._health}, "
            f"Strength: {self._strength}"
        )