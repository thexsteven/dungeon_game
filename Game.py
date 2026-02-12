from Player import Player 
from Monster import Monster 
from Room import Room
from RoomManager import RoomManager 

MIN_ROOMS = 1

class Game:
  def __init__(self):
    self.player = None
    self.room_manager = None
    self.num_rooms = 0

  def start(self):
    player_name = input("Enter your player's name: ")
    print(f"Welcome {player_name}, to the Dungeon Game!")

    while True:
      try:
        num_rooms = int(input("How many rooms do you want to create? "))
        if num_rooms <= 0:
          print("Enter a number bigger than 0.")
          continue
        break
      except ValueError:
        print("Please enter a valid number")

    self.player = Player(player_name)
    self.num_rooms = num_rooms

  def run_game(self):
    rooms = []
    for i in range(self.num_rooms):
      monster_name = input(f"Enter the name of monster for room {i+1}: ")
      monster = Monster(monster_name)
      room_name = f"Room_{i+1}"
      room = Room(room_name, monster)
      rooms.append(room)

    self.room_manager = RoomManager(rooms)

    while not self.room_manager.is_game_over() and self.player.health > 0:
      current_room = self.room_manager.get_current_room()
      if current_room is None:
        break
      print(current_room.get_status())
      action = input(f"Do you want to (f)ight the {current_room.monster.name} or (e)scape the room?")
      if action == "f":
        if current_room.fight_monster(self.player):
          self.room_manager.move_to_next_room()
      elif action == "e":
        current_room.escape_room(self.player)
        print(" \n")
      else:
        print("Invalid action! Please choose 'f' to fight or 'e' to escape.")

    if self.player.health <= 0:
      print(f"{self.player.name} has been defeated. Game is over!")
    elif self.room_manager.is_game_over():
      print(f"Congratulations {self.player.name}! You've defeated all monsters and won the Dungeon Game :)")