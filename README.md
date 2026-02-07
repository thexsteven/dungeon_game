# README.md

## Projektbeschreibung

Das ist ein textbasiertes Dungeon-Spiel für die Konsole. Der Spieler geht durch mehrere Räume und kämpft in jedem Raum gegen ein Monster. Man kann entweder kämpfen oder fliehen. Ziel ist es, alle Räume zu überleben ohne dass die Lebenspunkte auf 0 fallen.

## Installation und Ausführung

**Voraussetzungen:**

- Python 3.x muss installiert sein

**Spiel starten:**

```
python main.py
```

**Tests ausführen:**

```
python -m unittest discover -s . -p "test_*.py" -v
```

## Projektstruktur

[**main.py**](main.py)

Startpunkt des Programms. Hier wird das Spiel gestartet und die Wiederholungsschleife läuft.

[**Game.py**](Game.py)

Steuert den Spielablauf. Fragt Eingaben ab und koordiniert Player und RoomManager.

[**Player.py**](Player.py)

Die Spieler-Klasse mit Health, Strength und Methoden wie attack(), take_damage(), heal().

[**Monster.py**](Monster.py)

Die Monster-Klasse. Jedes Monster hat Health, Strength und kann angreifen.

[**RoomManager.py**](RoomManager.py)

Verwaltet alle Räume und prüft ob das Spiel vorbei ist.

[**Room.py**](Room.py)

Ein einzelner Raum mit einem Monster. Hier passiert der Kampf oder die Flucht.

**tests**

- [TestRoomManager.py](TestRoomManager.py)
- [TestPlayer.py](TestPlayer.py)

Unit Tests für Player und RoomManager. Testen Initialisierung, Grenzwerte und Methoden.

## Bekannte Einschränkungen

**Eingabevalidierung:**

Wenn man was anderes als "f" oder "e" eingibt, kommt nur eine Fehlermeldung. Das Spiel fragt dann nochmal.

**Keine Speicherfunktion:**

Man kann den Spielstand nicht speichern. Wenn man abbricht, muss man von vorne anfangen.

**Feste Schadenwerte beim Fliehen:**

Beim Fliehen verliert man immer genau 10 Lebenspunkte, egal wie stark das Monster ist.

**Zufallswerte:**

Die Angriffswerte sind zufällig. Manchmal ist ein Kampf viel leichter oder schwerer, das hängt vom Glück ab.

**Raumanzahl fest:**

Die Anzahl der Räume ist im Code festgelegt. Man kann das nicht beim Spielstart ändern.

## Technische Hinweise

Das Projekt nutzt objektorientierte Programmierung mit mehreren Klassen. Jede Klasse hat ihre eigene Datei.

Die Eingaben kommen über die Konsole mit input(). Der Spieler tippt "f" für Kampf oder "e" für Flucht.

Die Angriffs- und Lebenswerte werden beim Start mit Zufallszahlen generiert (random.randint). Das macht jedes Spiel ein bisschen anders.