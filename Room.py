class Room:
    """
    Represents a room in the dungeon containing a monster.
    """

    def __init__(self, name, monster):
        self._name = name
        self._monster = monster

    @property
    def name(self):
        """Returns the room's name."""
        return self._name

    @property
    def monster(self):
        """Returns the monster in this room."""
        return self._monster

    def get_status(self):
        """Returns a string describing the room and its monster."""
        return f"Room: {self._name}, {self._monster.get_status()}"

    def fight_monster(self, player):
        """Executes one round of combat between the player and the monster.

        The monster attacks first, then the player attacks. If the monster
        is defeated, the player regains half of the damage dealt.

        Returns:
            True if the monster is defeated, False otherwise.
        """
        monster_damage = self._monster.attack()
        player.take_damage(monster_damage)
        print(
            f"{self._monster.name} hits {player.name} for "
            f"{monster_damage} damage."
        )
        if player.health <= 0:
            print(
                f"{player.name} failed to defeat the "
                f"{self._monster.name} in room {self._name}."
            )
            return False
        damage_dealt = player.attack()
        self._monster.take_damage(damage_dealt)
        if not self._monster.is_alive():
            health_gained = int(damage_dealt / 2)
            player.regain_health(health_gained)
            print(
                f"{player.name} defeated the {self._monster.name} in room "
                f"{self._name} and has now {player.health} health.\n"
            )
            print(f"{player.name} gained {health_gained} health.")
            print(player.get_status())
            return True
        print(f"{player.name} is still alive.\n")
        return False

    def escape_room(self, player):
        """Player escapes the room, taking 10 damage."""
        player.take_damage(10)
        print(
            f"{player.name} escaped from room {self._name} "
            f"and took 10 damage.\n"
        )