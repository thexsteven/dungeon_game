# Prüfungsleistung - Dungeon Escape

In diesem Programmentwurf entwickeln Sie eine Python-Anwendung, die ein vereinfachtes Dungeon-Abenteuer darstellt. Dabei
steuert ein Spieler durch eine Reihe von Räumen, in denen Monster warten. Der Spieler kämpft gegen die Monster, um
aus dem Dungeon zu entkommen.

Sie erhalten im Folgenden alle zentralen Anforderungen (funktional und nicht-funktional) an das abzugebende Projekt. 
Lesen Sie alle Informationen gewissenhaft durch und geben Sie die genannten Leistungen im Moodle Kursraum ab.

## 1. Spiel-Logik
Das Spiel folgt folgender Logik durch Eingaben in die Kommandozeile:
1. Initialisierung des Spiels, d.h. der Nutzer definiert, wie viele Räume es geben soll, wie diese heißen und wie das 
    jeweilige Monster in diesem Raum heißt. In jedem Raum gibt es genau ein Monster. Zusätzlich werden jedem Monster 
    zufällig Lebenspunkte (zwischen 40 (inkl.) und 80 (inkl.)), sowie zufällige Stärkepunkte (zwischen 20 (inkl.) und 40 (inkl.))
    zugewiesen.
2. Start des Spiels: der Spieler wird namentlich begrüßt, erhält 100 Lebenspunkte und eine zufällige Stärke 
    zwischen 40 (inkl.) und 80 (inkl.) Punkten. Der Spieler hat maximal 100 Lebenspunkte.
3. Der Spieler betritt den ersten Raum und kämpft sich der Reihe nach durch alle Räume. Die Logik zum Kampf folgt im nächsten Abschnitt
4. Sobald der Spieler keine Lebenspunkte (health <= 0) mehr hat, ist das Spiel verloren.
5. Schafft der Spieler es bis durch den letzten Raum, ist das Spiel gewonnen.
6. Dem Spieler wird der Ausgang des Spiels mitgeteilt.

Zusätzlich zur Gesamtlogik gibt es folgende Spielmechanik in jedem Raum:
1. Auftritt des Monsters durch Konsolenausgabe.
2. Der Spieler kann nun entscheiden, ob er angreifen oder fliehen möchte. Wenn der Spieler fliehen möchte, erhält er
    10 Punkte Schaden auf seine Lebenspunkte.
3. Wenn der Spieler sich für einen Kampf entscheidet, passiert Folgendes:
   4. Angriff des Monsters: Der Spieler erhält automatisch Schaden in
    Höhe der Stärke des Monsters.
   5. Angriff des Spielers: Das Monster erhält Schaden in Höhe der Stärke des Spielers.
   6. Falls das Monster geschlagen wurde (health <= 0), ist der Kampf gewonnen und der Spieler kann den nächsten Raum 
       betreten.
   7. Falls das Monster noch lebt, muss so lange weitergekämpft werden, bis entweder der Spieler oder das Monster 
       geschlagen ist.
   8. Für den Fall, dass der Spieler das Monster besiegt, erhält er Lebenspunkte in Höhe der Hälfte des vom Monsters
       erlittenen Schadens. Z.B.: In einem Kampf erleidet ein Monster 60 Schadenspunkte. Hat der Spieler das Monster 
       geschlagen, so erhält der Spieler 60/2 = 30 Lebenspunkte auf seinen Gesundheitszustand gutgeschrieben.
9. Ist der letzte Raum erfolgreich durchlaufen (entweder Monster besiegt, oder erfolgreich geflohen), wird eine 
    Erfolgsmeldung auf der Konsole ausgegeben.

## 2. Pflicht-Klasse Player.py
Für das Spiel ist verpflichtend eine Klasse `Player` mit folgendem Aufbau zu erstellen:

### Instanzvariablen
Die Klasse `Player` enthält die folgenden privaten Instanzvariablen:

- `name`: Name des Spielers wird dem Konstruktor übergeben
- `health`: Gesundheitszustand des Spielers (soll standardmäßig auf den Wert 100 gesetzt werden)
- `strength`: Stärke des Spielers wird durch den Konstruktor gesetzt (zufällige Zahl zwischen 40 (inkl.) und 80 (inkl.))

### Methoden
Folgende Methoden sind zu implementieren:

- `__str__` soll folgenden String zurückgeben: `"Player <name> has <strength> strength and <health> health."`
- `take_damage(damage)` soll eine Zahl `damage` als Parameter erhalten und diesen vom aktuellen `health`
  Wert abziehen (Minimalwert: 0)
- `regain_health(health_regain)` soll eine Zahl `health_regain` als Parameter erhalten und diese auf die aktuelle
  `health` addieren (Maximalwert ist der Standardwert 100)

## 3. Anforderungen an das Spiel und den Code
- Die vorgegebene Spiel-Logik, sowie die vorgegebene Pflicht-Klasse müssen wie angegeben umgesetzt werden.
- Der abzugebende Code ist entsprechend den Prinzipien von OOP und Coding Conventions, wie in der Vorlesung behandelt 
   zu strukturieren.
- Das Spiel läuft vollständig über die Konsole ab und gibt zu passenden Zeitpunkten Informationen über den aktuellen 
   Spielablauf, sowie die beteiligten Spielfiguren aus.
- Die Nutzereingaben über die Konsole müssen in geeigneter Form überprüft und nur gültige Eingaben akzeptiert werden.
- Unit-Tests:
  - Es sollen mindestens eine Test-Datei für die vorgegebene Klasse sowie mindestens eine weitere Test-Datei für eine 
     andere zentrale Komponente Ihres Programms erstellt werden mit jeweils mindestens 3 Testfällen.
  - Verwenden Sie das Python-Framework unittest oder pytest.
  - Die Tests sollen sowohl typische Fälle als auch Randfälle abdecken.
- Das Spiel soll über eine Hauptdatei `main.py` gestartet werden und eine passende Startnachricht ausgeben.
- Kommentieren Sie Ihren Code in angebrachter Form. Einfache Anweisungen benötigen keine Kommentare, komplexere 
   Berechnungen, Entscheidungen, oder Abläufe müssen nachvollziehbar kommentiert werden.
- Erstellen Sie eine `README.md` Datei, um über Ihren Programmcode angemessen zu informieren. 
  - Kurze Projektbeschreibung: 3–5 Sätze zum Spiel, Setting, Ziel.
  - Installations- und Ausführungsanleitung: Wie startet man das Spiel? Wie führt man die Tests aus? 
  - Strukturübersicht: Kurze Erklärung der wichtigsten Dateien/Module und Klassen. 
  - Bekannte Einschränkungen / Bugs: Falls bekannte Fehler existieren, kurz beschreiben

## 4. Dokumentation (PDF-Datei)
Erstellen Sie neben dem Programmcode, den Tests und der README.md eine zusätzliche Projektdokumentation als PDF-Datei,
die neben Ihrem Namen und der Matrikelnummer folgende Aspekte enthält:

1. Konzeptbeschreibung: Kurzbeschreibung der Spielidee, Spiellogik und des typischen Spielablaufs.
2. Struktur- / Designskizze: Übersicht über die wichtigsten Klassen und Funktionen (z.B. als Text oder einfache Grafik).
3. Für jede zentrale Klasse: Zweck, Attribute und Methoden.
4. Testkonzept: 
   5. Welche Teile der Anwendung werden getestet? 
   6. Welche Arten von Fällen (Normalfälle, Randfälle) werden abgedeckt?
   7. Wie führen Sie die Tests aus?
8. Reflexion:
   9. Was waren Ihre größten Herausforderungen?
   10. Welche Fehler/Bugs sind aufgetreten und wie haben Sie diese gelöst?
   11. Wie sind Sie beim Entwurf der Klassen/Struktur vorgegangen?
   12. Welche Hilfsmittel (z.B. Foren, Google, IDE-Hilfestellung, ...) haben Sie verwendet (ein kurzer Absatz je Hilfsmittel):
      - Wie genau wurden diese eingesetzt?
      - Was haben Sie übernommen, was verworfen?
      - Was haben Sie dabei gelernt?

### Eigenständigkeitserklärung
Entsprechend Ihrer Prüfungsordnung §20, Absatz 5, ist die Dokumentation Ihres Projekts durch folgende Erklärung zur Eigenständigkeit der Leistung zu ergänzen:

>Ich versichere hiermit, dass ich die vorliegende Arbeit selbstständig verfasst
und keine anderen als die angegebenen Quellen und Hilfsmittel verwendet habe und diese Arbeit bei
keiner anderen Prüfung mit gleichem oder vergleichbarem Inhalt vorgelegt habe und diese bislang
nicht veröffentlicht wurde.

## 5. Abgabe
Geben Sie die folgenden Ergebnisse Ihrer Arbeit im Moodle Kursraum ab:

- Projektarchiv
  - .zip Datei Ihres Codes
  - Test-Dateien
  - README.md
  - keine unnötigen temporären Dateien, keine virtuellen Umgebungen
- Dokumentation (PDF Datei) strukturiert nach den oben vorgegebenen Kapiteln. 
      Namensschema der Datei: `INF25_Matrikelnummer_Name_Dokumentation.pdf`
- Abgabeformat: alles zusammen als .zip-Datei im Moodle-Kurs abgeben.
      Namensschema der zip-Datei: `INF25_Matrikelnummer_Name_Abgabe.zip

## 6. Bewertungsschema
Die Bewertung achtet auf folgende Aspekte (jeweils mit angegebener Maximalpunktzahl). 
In Summe können maximal 100 Punkte erreicht werden.

| Bewertungskategorie                        | Maximalpunkte |
|--------------------------------------------|---------------|
| Spiellogik und Funktionalität              | 30            |
| Pflichtklasse Player.py                    | 10            |
| OOP Design & Code-Struktur                 | 15            |
| Konsoleninteraktion und Eingabevalidierung | 10            |
| Unit-Tests                                 | 15            |
| Readme.md                                  | 5             |
| Projektdoku                                | 10            |
| Projektstruktur und Abgabeformalitäten     | 5             |