import unittest
from Player import Player, MAX_HEALTH, MIN_STRENGTH, MAX_STRENGTH


class TestPlayer(unittest.TestCase):
    """Tests for the Player class."""

    def setUp(self):
        """Creates a Player for each test."""
        self.player = Player("TestPlayer")

    def test_initial_health(self):
        """Tests that the player is created with maximum health."""
        self.assertEqual(self.player.health, MAX_HEALTH)

    def test_custom_health(self):
        """Tests that the player can be created with custom health."""
        custom_health = 75
        player = Player("CustomPlayer", custom_health)
        self.assertEqual(player.health, custom_health)

    def test_initial_strength_in_range(self):
        """Tests that the player's strength is within the valid range."""
        self.assertGreaterEqual(self.player.strength, MIN_STRENGTH)
        self.assertLessEqual(self.player.strength, MAX_STRENGTH)

    def test_take_damage(self):
        # Tests that take_damage reduces health correctly.
        initial_health = self.player.health
        damage = 30
        self.player.take_damage(damage)
        self.assertEqual(self.player.health, initial_health - damage)

    def test_take_damage_not_negative(self):
        # Tests that health cannot go below 0.
        self.player.take_damage(200)
        self.assertEqual(self.player.health, 0)

    def test_regain_health(self):
        # Tests that regain_health increases health correctly.
        self.player.take_damage(40)
        self.player.regain_health(20)
        self.assertEqual(self.player.health, MAX_HEALTH - 20)

    def test_regain_health_not_above_max(self):
        # Tests that health cannot exceed MAX_HEALTH.
        self.player.regain_health(50)
        self.assertEqual(self.player.health, MAX_HEALTH)

    def test_attack_returns_strength(self):
        # Tests that attack() returns the player's strength value.
        self.assertEqual(self.player.attack(), self.player.strength)

    def test_str_representation(self):
        # Tests that __str__ returns the correct format.
        expected = (
            f"Player TestPlayer has {self.player.strength} "
            f"strength and {MAX_HEALTH} health."
        )
        self.assertEqual(str(self.player), expected)

    def test_get_status(self):
        # Tests that get_status returns the correct status string.
        status = self.player.get_status()
        self.assertIn("TestPlayer", status)
        self.assertIn(str(MAX_HEALTH), status)


if __name__ == '__main__':
    unittest.main()
