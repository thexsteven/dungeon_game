# CHANGELOG

## [1.0.0] - 2026-02-17

### Player.py
- **KRITISCH**: `_strength` Attribut hinzugefügt (`random.randint(40, 80)` im Konstruktor)
- **KRITISCH**: `attack()` gibt jetzt `self._strength` zurück (nicht mehr zufällig pro Aufruf)
- **KRITISCH**: `__str__()` gibt jetzt `"Player <name> has <strength> strength and <health> health."` zurück
- Alle Attribute auf privat umgestellt: `_name`, `_health`, `_strength`
- `@property`-Dekoratoren für `name`, `health`, `strength` hinzugefügt
- Konstanten umbenannt: `MIN_ATTACK_DAMAGE` → `MIN_STRENGTH`, `MAX_ATTACK_DAMAGE` → `MAX_STRENGTH`
- `get_status()` zeigt jetzt auch Strength an
- PEP 8: Einrückung auf 4 Spaces korrigiert
- Docstrings für Klasse und alle Methoden hinzugefügt

### Monster.py
- Alle Attribute auf privat umgestellt: `_name`, `_health`, `_strength`
- `@property`-Dekoratoren für `name`, `health`, `strength` hinzugefügt
- PEP 8: Einrückung auf 4 Spaces korrigiert
- Docstrings für Klasse und alle Methoden hinzugefügt

### Room.py
- Alle Attribute auf privat umgestellt: `_name`, `_monster`
- `@property`-Dekoratoren für `name`, `monster` hinzugefügt
- Zugriffe auf Player/Monster-Attribute über Properties angepasst
- PEP 8: Einrückung auf 4 Spaces korrigiert
- Docstrings für Klasse und alle Methoden hinzugefügt

### RoomManager.py
- Alle Attribute auf privat umgestellt: `_rooms`, `_current_room_index`, `_game_over`
- `@property`-Dekoratoren für `current_room_index`, `game_over` hinzugefügt
- PEP 8: Einrückung auf 4 Spaces korrigiert
- Docstrings für Klasse und alle Methoden hinzugefügt

### Game.py
- Alle Attribute auf privat umgestellt: `_player`, `_room_manager`, `_num_rooms`
- Alle Zugriffe auf Player/RoomManager angepasst (Properties)
- PEP 8: Einrückung auf 4 Spaces korrigiert
- Docstrings für Klasse und alle Methoden hinzugefügt

### Tests
- **TestPlayer.py**: Angepasst an neue `_strength`-Logik, neue Tests für `strength`, `__str__()`, `attack()` hinzugefügt
- **TestRoomManager.py**: Komplett neu geschrieben mit korrekten Testnamen:
  - `test_initial_room_index_is_zero`
  - `test_get_current_room_returns_first_room`
  - `test_move_to_next_room_increments_index`
  - `test_get_current_room_after_move`
  - `test_game_over_after_last_room`
  - `test_get_current_room_with_empty_list`
- **TestRoom.py**: Neu erstellt mit MockMonster/MockPlayer:
  - `test_fight_monster_player_wins`
  - `test_escape_room_deals_10_damage`
  - `test_fight_monster_hp_regeneration`
