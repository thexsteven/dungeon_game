class RoomManager:
  def __init__(self, rooms):
    self.rooms = rooms
    self.current_room_index = 0
    #self.game_over = False

  def get_current_room(self):
    if self.current_room_index < len(self.rooms):
      return self.rooms[self.current_room_index]
    else:
      return None
    
  def move_to_next_room(self):
    if self.current_room_index < len(self.rooms) - 1:
      self.current_room_index += 1
      print(f"\n Moved to room {self.current_room_index + 1}: {self.get_current_room().name}")
    else:
      print("Congratulations! You won the Dungeon game :)")

  def is_game_over(self):
    return self.game_over