# Konstante Werte vom Player
MAX_HEALTH = 100
MIN_ATTACK_DAMAGE = 40
MAX_ATTACK_DAMAGE = 80

class Player:
  def __init__(self, name, health=MAX_HEALTH):
    self.name = name
    self.health = health
    