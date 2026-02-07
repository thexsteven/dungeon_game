class Room:
  def __init__(self, name, monster):
    self.name = name
    self.monster = monster

  def get_status(self):
    return f"Room: {self.name}, {self.monster.get_status()}"