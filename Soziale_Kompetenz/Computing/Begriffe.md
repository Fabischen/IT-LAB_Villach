# LAP-Fragenkatalog

## 1. Computing
**Definition:**  
Computing bezeichnet allgemein das Rechnen mit Computern bzw. das Verwenden von Computern zur Lösung von Problemen. Es umfasst alle Akticitäten rund um das Entwickeln, Ausführen und Analysieren von Programmen.

**Beispiel:**
- Entwicklung einer Wetter-App, die Wetterdaten sammelt und analysiert.
- Betrieb eines Servers, der eine Webseite hostet.

**Wichtig:**  
*Computing* ist ein Überbegriff, der Informatik, Softwareentwicklung, Hardwaredesign, Datenverarbeitung uvm. umfasst.

<br>

## 2. Computational Thinking
**Definition:**  
*Computational Thinking* ist eine Denkweise, bei der Probleme so analysiert und gelöst werden, dass sie von einem Computer effizient bearbeitet werden können.

**Zentrale Konzepte:**
- Zerlegen (Decomposition)
- Mustererkennung (Pattern Recognition)
- Abstraktion
- Algorithmisches Denken

**Beispiel:**  
Beim Planen eines Rezepts: Schrittweise Anweisungen (Algorithmus) formulieren, die jeder (oder ein Roboter) befolgen kann.

**Unterschied zu 'Computing':**  
*Computational Thinking* ist die Denkweise, die hinter *Computing* steckt – also eher kognitiv-methodisch, während „Computing“ die praktische Umsetzung umfasst.

<br>

## 3. Programm
**Definition:**  
Ein Programm ist eine Abfolge von Anweisungen, die von einem Computer ausgeführt werden, um eine bestimmte Aufgabe zu erfüllen.

**Beispiel:**  
Ein Taschenrechnerprogramm, das zwei Zahlen addiert...
```py
a = 5
b = 3
print(a + b)
```

**Unterschied zu Code:**  
Ein Programm ist das gesamte System oder die Anwendung, während *Code* die konkreten Textzeilen in einer Programmiersprache sind.

<br>

## 4. Code / Quellcode
**Definition:**  
*Code* bzw. *Quellcode* ist der Text eines Programms, geschrieben in einer Programmiersprache wie Python, Java oder C++.

**Beispiel:**
```py
for i in range(5):
  print("Hello World")
```

**Unterschiede:**
- *Quellcode* ist spezifischer: meist der Originaltext vor der Kompilierung.
- *Code* ist allgemeiner und kann auch Maschinencode oder Skriptcode meinen.

## 5. Maschinencode
**Definition:**  
Maschinencode ist der in 0 und 1 übersetzte, direkt vom Prozessor ausführbare Code (Binärcode) - Zahl 13 in binär `1101`.

**Verhältnis zu Quellcode:**  
Quellcode wird durch einen Compiler oder Interpreter in Maschinencode übersetzt, damit der Computer ihn ausführen kann.

<br>

## 6. Programmbeschreibung / Programmspezifizierung
**Definition:**
- **Programmbeschreibung:** Eine (oft informelle) Erklärung, was ein Programm tut oder tun soll.
- **Programmspezifizierung (Spezifikation):** Eine formale Beschreibung der Anforderungen und des erwarteten Verhaltens eines Programms – oft in mathematischer oder pseudocodehafter Form.

**Beispiel für eine Programmbeschreibung:**  
*Das Programm berechnet den Mittelwert einer Liste von Zahlen.*

**Beispiel für eine Spezifikation:**
```text
Eingabe: Liste L mit n Zahlen (n => 1)
Ausgabe: float m = (Summe aller Elemente von L) / n
```

**Unterschied:**
- *Beschreibung* = natürlichsprachlich, oft vage.
- *Spezifikation* = formal, eindeutig, überprüfbar.

<br>

## 7. Unterschied: Formale Sprache vs. Natürliche Sprache
| Merkmal       | Formale Sprache                  | Natürliche Sprache                          |
| ------------- | ---------------------------------| ------------------------------------------- |
| Verwendung    | Mathematik, Progammierung        | Alltag, Kommunikation                       |
| Eindeutigkeit | Hoch - eindeutig interpretierbar | Gering - oft mehrdeutig                     |
| Grammatik     | Strikt definiert                 | Flexibel, kontextabhängig                   |
| Beispiel      | `if x > 0 then print("Positiv")` | "Falls x größer null ist, drucke 'Positiv'" |
| Ziel          | Präzision, Automatisierbarkeit   | Verständlichkeit für Menschen               |

**Fazit:**  
Formale Sprachen (wie Programmiersprachen) sind für Computer gedacht – klar und eindeutig. Natürliche Sprachen (wie Deutsch oder Englisch) sind für Menschen gemacht – flexibel, aber oft ungenau.

<br>

## 8. Problemdekomposition
**Definition:**  
Das Zerlegen eines komplexen Problems in kleinere, besser handhabbare Teilprobleme.

**Arten:**
- **Daten-Dekomposition:** Zerlegung basierend auf Daten (zB. Teile einer Liste separat verarbeiten)
- **Prozess-Dekomposition:** Zerlegung anhand der Teilfunktionen oder Schritte
- **Komplexitäts-Dekomposition:** Zerlegung, um kognitive oder technische Komplexität zu verringern

**Beispiel:**  
Ein Onlineshop-System:
- Daten: Produkte, Benutzer, Bestellungen
- Prozesse: Registrierung, Produktsuche, Warenkorb, Bezahlung

**Zweck:**  
Erleichtert Planung, Wartung, Wiederverwendung und Testbarkeit.

<br>

## 9. Mustererkennung (Pattern Recognition)
**Definition:**  
Das Identifizieren von wiederkehrenden Strukturen, Regeln oder Ähnlichkeiten innerhalb von Daten oder Problemen.

**Beispiel:**
- Erkennen, dass bei jeder Eingabe eines Passworts zuerst die Länge geprüft wird
- In Zahlenreihen das Muster '+2' entdecken: 2, 4, 6, 8, 10...

**Rolle im Computational Thinking:**  
Hilft, generische Lösungen zu entwickeln oder Algorithmen zu optimieren.

<br>

## 10. Abstraktion
**Definition:**  
Das Herausfiltern der wesentlichen Informationen und das Weglassen unwichtiger Details.

**Beispiel:**  
Beim Programmieren einer Spielfigur interessieren nur Position und Richtung, nicht ihre Farbe oder Kleidung (sofern irrelevant für die Steuerung).

**Ziel:**  
- Allgemeinere, wiederverwendbare Modelle oder Algorithmen schaffen
- Komplexität reduzieren

**Unterschied zur Dekomposition:**
- *Dekomposition:* "Was sind die Einzelteile?"
- *Abstraktion:* "Was davon ist relevant?"

<br>

## 11. Algorithmus
**Definition:**  
Eine endliche, klar definierte Folge von Anweisungen zur Lösung eines Problems.

**Merkmale:**  
Endlichkeit, Eindeutigkeit, Ausführbarkeit, Allgemeinheit

**Beispiel (in Alltagssprache):**
> Schäle eine Banane. Schneide sie in Scheiben. Git sie in eine Schüssel.

**Beispiel (technisch):**
> Ein Sortieralgorithmus (zB. Bubble Sort) sortiert eine Liste von Zahlen durch wiederholten Vergleich und Tausch benachbarter Elemente.

<br>

## 12. Sequenz
**Definition:**  
Eine lineare Abfolge von Anweisungen, die nacheinander ausgeführt werden.

**Beispiel (Pseudocode):**
```md
1. Eingabe: Zahl A
2. Eingabe: Zahl B
3. C = A + B
4. Ausgabe: C
```

**Rolle im Algorithmus:**  
Sequenzen sind der Grundbaustein eines Algorithmus – neben *Verzweigungen (if/else)* und *Wiederholungen (loops)*.

<br>

## 13. Ablaufdiagramm / Flussdiagramm / Pseudocode

### Ablaufdiagramm (Flowchart / Flussdiagramm)

**Definition:**  
Grafische Darstellung eines Prozesses oder Algorithmus mithilfe von Symbolen (zB. Start, Entscheidung, Prozess, Ausgabe).

**Beispiel:**
```md
[Start] → [Eingabe Zahl] → [Ist Zahl > 0?]
                           ↓Ja       Nein↓
              [Ausgabe: positiv]   [Ausgabe: nicht positiv]
```

**Zweck:**  
Visualisiert den logischen Ablauf. Gut geeignet für Planung und Kommunikation.

### Pseudocode
**Definition:**  
Textuelle Beschreibung eines Algorithmus, die sich an Programmiersprachen orientiert, aber nicht formal ausführbar ist.

**Beispiel:**
```text
Lies eine Zahl ein
Wenn Zahl > 0 dann
  Gib "positiv" aus
Sonst
  Gib "nicht positiv" aus
```

**Unterschiede:**
| Merkmal        | Ablaufdiagramm      | Pseudocode                         |
| -------------- | ------------------- | ---------------------------------- |
| Form           | Visuell (Diagramm)  | Textuell                           |
| Ziel           | Veranschaulichung   | Vorbereitung auf Programm          |
| Einsatzbereich | Frühphase / Planung | Dokumentation / Algorithmusentwurf |