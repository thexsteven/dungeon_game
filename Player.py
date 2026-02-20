import random

# Constant values for the player
MAX_HEALTH = 100
MIN_STRENGTH = 40
MAX_STRENGTH = 80


class Player:
    """
    Represents the player in the dungeon game.
    """

    def __init__(self, name, health=MAX_HEALTH):
        self._name = name
        self._health = health
        self._strength = random.randint(MIN_STRENGTH, MAX_STRENGTH)

    @property
    def name(self):
        """Returns the player's name."""
        return self._name

    @property
    def health(self):
        """Returns the player's current health."""
        return self._health

    @property
    def strength(self):
        """Returns the player's strength."""
        return self._strength

    def __str__(self):
        return (
            f"Player {self._name} has {self._strength} strength "
            f"and {self._health} health."
        )

    def take_damage(self, damage):
        """Reduces health by the given damage amount. Health cannot go below 0."""
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def attack(self):
        """Returns the player's strength as attack damage."""
        return self._strength

    def regain_health(self, health_regain):
        """Increases health by the given amount. Health cannot exceed MAX_HEALTH."""
        self._health += health_regain
        if self._health > MAX_HEALTH:
            self._health = MAX_HEALTH

    def get_status(self):
        """Returns a string describing the player's current status."""
        return (
            f"Player {self._name}, Health: {self._health}, "
            f"Strength: {self._strength}"
        )