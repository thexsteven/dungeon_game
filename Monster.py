import random

# Monster constants
MIN_MONSTER_HEALTH = 40
MAX_MONSTER_HEALTH = 80
MIN_MONSTER_STRENGTH = 20
MAX_MONSTER_STRENGTH = 40

class Monster:
  def __init__(self, name):
    self.name = name
    self.health = random.randint(MIN_MONSTER_HEALTH, MAX_MONSTER_HEALTH)
    self.strength = random.randint(MIN_MONSTER_STRENGTH, MAX_MONSTER_STRENGTH)