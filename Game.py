from Player import Player
from Monster import Monster
from Room import Room
from RoomManager import RoomManager

MIN_ROOMS = 1


class Game:
    """
    Main game class that orchestrates the dungeon game.
    """

    def __init__(self):
        self._player = None
        self._room_manager = None
        self._num_rooms = 0

    def start(self):
        # Initializes the game by getting player name and number of rooms.
        player_name = input("Enter your player's name: ")
        print(f"Welcome {player_name}, to the Dungeon Game!")

        while True:
            try:
                num_rooms = int(
                    input("How many rooms do you want to create? ")
                )
                if num_rooms < MIN_ROOMS:
                    print("Enter a number bigger than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

        self._player = Player(player_name)
        self._num_rooms = num_rooms

    def run_game(self):
        # Runs the main game loop through all rooms.
        rooms = []
        for room_number in range(1, self._num_rooms + 1):
            monster_name = input(
                f"Enter the name of monster for room {room_number}: "
            )
            monster = Monster(monster_name)
            room_name = f"Room_{room_number}"
            room = Room(room_name, monster)
            rooms.append(room)

        self._room_manager = RoomManager(rooms)

        while (not self._room_manager.is_game_over()
               and self._player.health > 0):
            current_room = self._room_manager.get_current_room()
            if current_room is None:
                break
            print(current_room.get_status())
            action = input(
                f"Do you want to (f)ight the {current_room.monster.name} "
                f"or (e)scape the room?"
            ).strip().lower()
            if action == "f":
                if current_room.fight_monster(self._player):
                    self._room_manager.move_to_next_room()
            elif action == "e":
                current_room.escape_room(self._player)
                if self._player.health > 0:
                    self._room_manager.move_to_next_room()
                print()
            else:
                print(
                    "Invalid action! Please choose "
                    "'f' to fight or 'e' to escape."
                )

        if self._player.health <= 0:
            print(
                f"{self._player.name} has been defeated. Game is over!"
            )
        elif self._room_manager.is_game_over():
            print(
                f"Congratulations {self._player.name}! You've defeated "
                f"all monsters and won the Dungeon Game :)"
            )