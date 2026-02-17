import unittest
from RoomManager import RoomManager


class MockRoom:
    """A mock room class for testing the RoomManager."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Returns the mock room's name."""
        return self._name


class TestRoomManager(unittest.TestCase):
    """Tests for the RoomManager class."""

    def setUp(self):
        """Creates a RoomManager with mock rooms for each test."""
        self.rooms = [
            MockRoom("Room1"),
            MockRoom("Room2"),
            MockRoom("Room3")
        ]
        self.room_manager = RoomManager(self.rooms)

    def test_initial_room_index_is_zero(self):
        """Tests that the initial room index is 0."""
        self.assertEqual(self.room_manager.current_room_index, 0)

    def test_get_current_room_returns_first_room(self):
        """Tests that get_current_room returns the first room initially."""
        current_room = self.room_manager.get_current_room()
        self.assertEqual(current_room.name, "Room1")

    def test_move_to_next_room_increments_index(self):
        """Tests that move_to_next_room increments the room index."""
        self.room_manager.move_to_next_room()
        self.assertEqual(self.room_manager.current_room_index, 1)

    def test_get_current_room_after_move(self):
        """Tests that get_current_room returns the correct room after moving."""
        self.room_manager.move_to_next_room()
        current_room = self.room_manager.get_current_room()
        self.assertEqual(current_room.name, "Room2")

    def test_game_over_after_last_room(self):
        """Tests that moving past the last room sets game_over to True."""
        self.room_manager.move_to_next_room()  # -> Room2
        self.room_manager.move_to_next_room()  # -> Room3
        self.assertFalse(self.room_manager.is_game_over())
        self.room_manager.move_to_next_room()  # past last room
        self.assertTrue(self.room_manager.is_game_over())

    def test_get_current_room_with_empty_list(self):
        """Tests that get_current_room returns None for an empty room list."""
        empty_manager = RoomManager([])
        self.assertIsNone(empty_manager.get_current_room())


if __name__ == '__main__':
    unittest.main()
