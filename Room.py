class Room:
  def __init__(self, name, monster):
    self.name = name
    self.monster = monster

  def get_status(self):
    return f"Room: {self.name}, {self.monster.get_status()}"
  
  def fight_monster(self, player):
    player.take_damage(self.monster.attack()) 
    damage_dealt = player.attack() # den durch den Spieler verursachten Schaden speichern
    self.monster.take_damage(damage_dealt)
    if not self.monster.is_alive():
      health_gained = int(damage_dealt/2) 
      player.regain_health(health_gained)
      print(f"{player.name} defeated the {self.monster.name} in room {self.name} \n")
      print(f"{player.name} gained {health_gained} health.")
      player.get_status()
      return True
    elif player.health > 0:
      print(f"{player.name} is still alive. \n")
      return False
    else:
      print(f"{player.name} failed to defeat the {self.monster.name} in room {self.name}.")
      return False