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

  
