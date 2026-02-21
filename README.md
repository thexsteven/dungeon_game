# README.md

## Project Description

A text-based dungeon game for the console. The player navigates through multiple rooms and fights a monster in each room. You can either fight or escape. The goal is to survive all rooms without your health dropping to 0.

## Installation and Setup

**Prerequisites:**

- Python 3.x must be installed

**Start the game:**

```
python main.py
```

**Run tests:**

```
python -m unittest discover -s tests -p "Test*.py" -v
```

## Project Structure

[**main.py**](main.py)

Entry point of the program. Starts the game and runs the replay loop.

[**Game.py**](Game.py)

Controls the game flow. Handles user input and coordinates Player and RoomManager.

[**Player.py**](Player.py)

The player class with health, strength and methods like attack(), take_damage(), regain_health().

[**Monster.py**](Monster.py)

The monster class. Each monster has health, strength and can attack.

[**RoomManager.py**](RoomManager.py)

Manages all rooms and checks whether the game is over.

[**Room.py**](Room.py)

A single room containing a monster. Combat and escape happen here.

**tests**

- [tests/TestPlayer.py](tests/TestPlayer.py)
- [tests/TestRoom.py](tests/TestRoom.py)
- [tests/TestRoomManager.py](tests/TestRoomManager.py)

Unit tests for Player, Room and RoomManager. Testing initialization, edge cases and methods.

## Known Limitations

**Input Validation:**

If you enter something other than "f" or "e", an error message is shown. The game then asks again.

**No Save Feature:**

The game state cannot be saved. If you quit, you have to start over.

**Fixed Escape Damage:**

When fleeing, you always lose exactly 10 health points, regardless of how strong the monster is.

**Random Values:**

Attack values are random. Sometimes a fight is much easier or harder, depending on luck.

**Interactive Gameplay:**

The number of rooms is freely selectable at the start and is set via console input.

## Technical Notes

The project uses object-oriented programming with multiple classes. Each class has its own file.

Input is handled via the console using input(). The player types "f" to fight or "e" to flee.

Attack and health values are generated at startup using random numbers (random.randint). This makes each game slightly different.