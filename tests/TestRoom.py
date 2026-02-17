import unittest
from Room import Room


class MockMonster:
    """A mock monster class for testing the Room class."""

    def __init__(self, name, health, strength):
        self._name = name
        self._health = health
        self._strength = strength

    @property
    def name(self):
        """Returns the mock monster's name."""
        return self._name

    @property
    def health(self):
        """Returns the mock monster's health."""
        return self._health

    def attack(self):
        """Returns the mock monster's strength as damage."""
        return self._strength

    def take_damage(self, damage):
        """Reduces health by the given damage amount."""
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def is_alive(self):
        """Returns True if health is above 0."""
        return self._health > 0

    def get_status(self):
        """Returns a status string."""
        return (
            f"Monster: {self._name}, Health: {self._health}, "
            f"Strength: {self._strength}"
        )


class MockPlayer:
    """A mock player class for testing the Room class."""

    def __init__(self, name, health, strength):
        self._name = name
        self._health = health
        self._strength = strength

    @property
    def name(self):
        """Returns the mock player's name."""
        return self._name

    @property
    def health(self):
        """Returns the mock player's health."""
        return self._health

    def attack(self):
        """Returns the mock player's strength as damage."""
        return self._strength

    def take_damage(self, damage):
        """Reduces health by the given damage amount."""
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def regain_health(self, health_regain):
        """Increases health by the given amount, capped at 100."""
        self._health += health_regain
        if self._health > 100:
            self._health = 100

    def get_status(self):
        """Returns a status string."""
        return (
            f"Player {self._name}, Health: {self._health}, "
            f"Strength: {self._strength}"
        )


class TestRoom(unittest.TestCase):
    """Tests for the Room class."""

    def test_fight_monster_player_wins(self):
        """Tests that a strong player defeats a weak monster."""
        monster = MockMonster("Goblin", health=30, strength=10)
        player = MockPlayer("Hero", health=100, strength=50)
        room = Room("TestRoom", monster)

        result = room.fight_monster(player)

        self.assertTrue(result)
        self.assertFalse(monster.is_alive())

    def test_escape_room_deals_10_damage(self):
        """Tests that escaping a room deals exactly 10 damage."""
        monster = MockMonster("Goblin", health=50, strength=20)
        player = MockPlayer("Hero", health=100, strength=40)
        room = Room("TestRoom", monster)

        room.escape_room(player)

        self.assertEqual(player.health, 90)

    def test_fight_monster_hp_regeneration(self):
        """Tests that the player gains half the damage dealt after winning.

        Setup: Monster has 20 HP, 10 strength. Player has 60 HP, 40 strength.
        Round: Player takes 10 damage (60->50), deals 40 to monster (dies).
        Regen: Player gains 40/2 = 20 health (50->70).
        """
        monster = MockMonster("Goblin", health=20, strength=10)
        player = MockPlayer("Hero", health=60, strength=40)
        room = Room("TestRoom", monster)

        room.fight_monster(player)

        self.assertEqual(player.health, 70)


if __name__ == '__main__':
    unittest.main()
