class RoomManager:
    """Manages the sequence of rooms in the dungeon.

    Attributes:
        _rooms: List of Room instances.
        _current_room_index: Index of the current room.
        _game_over: Whether the game is over (all rooms cleared).
    """

    def __init__(self, rooms):
        self._rooms = rooms
        self._current_room_index = 0
        self._game_over = False

    @property
    def current_room_index(self):
        """Returns the index of the current room."""
        return self._current_room_index

    @property
    def game_over(self):
        """Returns whether the game is over."""
        return self._game_over

    def get_current_room(self):
        """Returns the current room, or None if no rooms remain."""
        if self._current_room_index < len(self._rooms):
            return self._rooms[self._current_room_index]
        else:
            return None

    def move_to_next_room(self):
        """Advances to the next room. Sets game_over if all rooms are cleared."""
        if self._current_room_index < len(self._rooms) - 1:
            self._current_room_index += 1
            print(
                f"\n Moved to room {self._current_room_index + 1}: "
                f"{self.get_current_room().name}"
            )
        else:
            self._game_over = True

    def is_game_over(self):
        """Returns True if all rooms have been cleared."""
        return self._game_over