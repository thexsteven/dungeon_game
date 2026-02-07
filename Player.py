import random

# Konstante Werte vom Player
MAX_HEALTH = 100
MIN_ATTACK_DAMAGE = 40
MAX_ATTACK_DAMAGE = 80

class Player:
  def __init__(self, name, health=MAX_HEALTH):
    self.name = name
    self.health = health

  def __str__(self):
    return f"Player {self.name} has {self.health} health."
    
  def take_damage(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0

  # Zufälligen Wert für Attacken des Players
  def attack(self):
    random_attack = random.randint(MIN_ATTACK_DAMAGE, MAX_ATTACK_DAMAGE)
    return random_attack
  
  def regain_health(self, health_regain):
    self.health += health_regain
    if self.health > MAX_HEALTH:
      self.health = MAX_HEALTH

  def get_status(self):
    return f"Player {self.name}, Health: {self.health}"