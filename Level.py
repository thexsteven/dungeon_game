class RoomManager:
  def __init__(self, rooms):
    self.rooms = rooms
    self.current_room_index = 0

  def get_current_room(self):
    if self.current_room_index < len(self.rooms):
      return self.rooms[self.current_room_index]
    else:
      return None