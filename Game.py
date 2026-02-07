from Player import Player 
from Monster import Monster 
from Room import Room
from RoomManager import RoomManager 

MIN_ROOMS = 1

class Game:
  def __init__(self):
    self.player = None
    self.RoomManager = None

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

    self.RoomManager = RoomManager(rooms)