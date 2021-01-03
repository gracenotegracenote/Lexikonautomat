# Basismodul Computerlinguistik: Implementierungsaufgabe Lexikonautomat

## Allgemeine Beschreibung

Das vorliegende Projekt stellt eine Implementierung von Daciuk-Algorithmus zur Konstruktion eines minimalen 
Lexikonautomaten dar.

Es wurden folgende Erweiterungen implementiert:
1. Off-Line-Konstruktion: Berechnung des minimalen deterministischen Automaten für eine beliebige alphabetisch sortierte Wortliste.
1. On-Line-Konstruktion: das Hinzufügen und Löschen eines beliebigen Worts ohne Einhaltung der lexikographischen Ordnung.
1. Sprache des Automaten: 
    11. mit einem Eingabestring w kann getestet werden, ob w im Lexikon ist;
    11. alle im Automaten enthaltene Wörter können in Form einer Wortliste ausgegeben werden.
1. Grafische Darstellung: Erstellung einer pdf-Datei, die den Lexikonautomaten graphisch darstellt.

## Ausführung

Das Projekt kann durch den Aufruf der Main-Datei gestartet werden:
````
python main.py
````

Eine interaktive Session wird in der Konsole gestartet. Der Benutzer kann eine von 6 Operationen auswählen:

##### (1) Wort abfragen

Beim Eingeben einer Eins (1) in die Konsole wird die erste Operation aufgerufen. Der Benutzer wird gebeten,
ein beliebiges Wort zu tippen. Nach dem Drücken der Eingabetaste (Enter) wird das eingegebene Wort im 
Lexikonautomaten gesucht. Der Benutzer bekommt eine Rückmeldung, ob das eingegebene Word im Lexikonautomaten 
vorhanden ist (siehe Erweiterung "Sprache des Automaten - Eingabestring").

##### (2) Automatensprache anzeigen

Diese Option startet eine Tiefensuche im Lexikonautomaten und gibt alle Wörter in die Konsole aus
(siehe Erweiterung "Sprache des Automaten - alle Wörter").

##### (3) Automat zeichnen

Es werden eine gv- und eine pdf-Datei im Ordner des Projektes angelegt, die die Zeichnung des aktuellen
Lexikonautomaten speichern (siehe Erweiterung "Grafische Darstellung"). Die weißen Knoten sind nicht finale Zustände, 
die blauen sind final.
Für das Zeichen wird die Bibliothek Graphviz verwendet, deswegen ist es für die einwandfreie Benutzung dieser 
Erweiterung notwendig, das Graphviz Programm lokal zu installieren. Hier der Link zum Herunterladen der 
Installationsdatei für Windows: [Graphviz](http://ssw.jku.at/Teaching/Lectures/PI2/2018/Graphviz.html).

##### (4) Wort hinzufügen

Nach der Auswahl der Option (4) kann der Benutzer ein Wort eingeben, das er im Lexikonautomaten speichern will. 
Nach dem Speichern bekommt der Benutzer eine Rückmeldung in der Konsole (siehe Erweiterung "On-Line-Konstruktion").

##### (5) Wort löschen

Hier wird eine Löschoperation aufgerufen, die das vom Benutzer eingegebene Wort aus dem Lexikonautomaten entfernt. 
Wenn das eingegebene Wort im Lexikonautomaten nicht enthalten ist, bekommt der Benutzer eine
entsprechende Rückmeldung, sowie auch nach einem erfolgreichen Löschen (siehe Erweiterung "On-Line-Konstruktion").

##### (0) Hauptmenü / Abbrechen

Diese Option stoppt die Ausführung des Programms, wenn man sich im Hauptmenü befindet. In allen anderen 
Fällen dient die Eingabe von Null (0) dem Rückkehr zum Hauptmenü.

## Autorin

* Liudmila Kachurina
l.kachurina@campus.lmu.de