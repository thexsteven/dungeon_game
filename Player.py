import random

# Konstante Werte vom Player
MAX_HEALTH = 100
MIN_ATTACK_DAMAGE = 40
MAX_ATTACK_DAMAGE = 80

class Player:
  def __init__(self, name, health=MAX_HEALTH):
    self.name = name
    self.health = health
    self.strength = random.randint(MIN_ATTACK_DAMAGE, MAX_ATTACK_DAMAGE)

  def __str__(self):
    return f"Player {self.name} has {self.health} health and {self.strength} strength."
    
  def take_damage(self, damage)
    self.health -= damage
    if self.health < 0:
      self.health = 0