import unittest
from Player import Player, MAX_HEALTH, MIN_ATTACK_DAMAGE, MAX_ATTACK_DAMAGE


class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        """Erstellt einen Player für jeden Test."""
        self.player = Player("TestPlayer")
    
    def test_initial_health(self):
        """Testet, ob der Player mit der maximalen Gesundheit erstellt wird."""
        self.assertEqual(self.player.health, MAX_HEALTH)
    
    def test_custom_health(self):
        """Testet, ob der Player mit einem benutzerdefinierten Gesundheitswert erstellt wird."""
        custom_health = 75
        player = Player("CustomPlayer", custom_health)
        self.assertEqual(player.health, custom_health)
    
    def test_take_damage(self):
        """Testet, ob take_damage die Gesundheit reduziert."""
        initial_health = self.player.health
        damage = 30
        self.player.take_damage(damage)
        self.assertEqual(self.player.health, initial_health - damage)
    
    def test_take_damage_not_negative(self):
        """Testet, dass die Gesundheit nicht unter 0 fällt."""
        self.player.take_damage(200)
        self.assertEqual(self.player.health, 0)
    
    def test_regain_health(self):
        """Testet, ob regain_health die Gesundheit erhöht."""
        self.player.take_damage(40)
        self.player.regain_health(20)
        self.assertEqual(self.player.health, MAX_HEALTH - 20)
    
    def test_regain_health_not_above_max(self):
        """Testet, dass die Gesundheit nicht über MAX_HEALTH steigt."""
        self.player.regain_health(50)
        self.assertEqual(self.player.health, MAX_HEALTH)
    
    def test_get_status(self):
        """Testet, ob get_status den richtigen Status zurückgibt."""
        status = self.player.get_status()
        self.assertIn("TestPlayer", status)
        self.assertIn(str(MAX_HEALTH), status)
    
    def test_attack_returns_value_in_range(self):
        """Testet, ob attack() einen Wert im gültigen Bereich zurückgibt."""
        attack_value = self.player.attack()
        self.assertGreaterEqual(attack_value, MIN_ATTACK_DAMAGE)
        self.assertLessEqual(attack_value, MAX_ATTACK_DAMAGE)


if __name__ == '__main__':
    unittest.main()
