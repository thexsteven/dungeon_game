import unittest
from RoomManager import RoomManager


class MockRoom:
    """Eine Mock-Klasse für Räume zum Testen."""
    def __init__(self, name):
        self.name = name


class TestRoomManager(unittest.TestCase):
    
    def setUp(self):
        """Erstellt einen RoomManager mit Mock-Räumen für jeden Test."""
        self.rooms = [
            MockRoom("Room1"),
            MockRoom("Room2"),
            MockRoom("Room3")
        ]
        self.room_manager = RoomManager(self.rooms)
    
    def test_initial_room_index(self):
        """Testet, ob der aktuelle Raumindex initial 0 ist."""
        self.assertEqual(self.room_manager.current_room_index, 0)
    
    def test_get_current_room(self):
        """Testet, ob get_current_room den ersten Raum zurückgibt."""
        current_room = self.room_manager.get_current_room()
        self.assertEqual(current_room.name, "Room1")
    
    def test_move_to_next_room(self):
        """Testet, ob move_to_next_room den Index erhöht."""
        self.room_manager.move_to_next_room()
        self.assertEqual(self.room_manager.current_room_index, 1)
    
    def test_move_to_next_room_updates_room(self):
        """Testet, ob nach dem Wechsel der richtige Raum zurückgegeben wird."""
        self.room_manager.move_to_next_room()
        current_room = self.room_manager.get_current_room()
        self.assertEqual(current_room.name, "Room2")
    
    def test_cannot_move_past_last_room(self):
        """Testet, dass nicht über das letzte Zimmer hinausgegangen werden kann."""
        # Bewege zu allen Räumen
        self.room_manager.move_to_next_room()  # Index 1
        self.room_manager.move_to_next_room()  # Index 2
        # Versuche noch einmal zu bewegen - sollte nicht über Index 2 hinausgehen
        self.room_manager.move_to_next_room()
        self.assertEqual(self.room_manager.current_room_index, 2)
    
    def test_get_current_room_returns_none_when_no_rooms(self):
        """Testet, dass get_current_room None zurückgibt, wenn keine Räume vorhanden sind."""
        empty_manager = RoomManager([])
        self.assertIsNone(empty_manager.get_current_room())


if __name__ == '__main__':
    unittest.main()
