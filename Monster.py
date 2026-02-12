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

  def attack(self):
    return self.strength
  
  def take_damage(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0
    print(f"{self.name} took {damage} damage and now has {self.health} health.")

  def is_alive(self):
    return self.health > 0
  
  def get_status(self):
    return f"Monster: {self.name}, Health: {self.health}, Strength: {self.strength}"