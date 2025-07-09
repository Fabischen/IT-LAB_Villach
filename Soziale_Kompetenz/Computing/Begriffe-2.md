# Begriffe (Definition & Beispiele)


## 1. Datentypen
**Definition:** Ein *Datentyp* bestimmt, welche Art von Werten eine Variable annehmen kann, zB. ganze Zahlen, Kommazahlen oder Zeichenketten.

**Beispiele:**
- *Integer:* Ganze Zahl `42`, `-7`
- *Float:* Kommazahl `3.14`, `-0.01`
- *String:* Zeichenkette `Hello World`
- *Boolean:* Wahrheitswert `true`, `false`


## 2. Vaiable
**Definition:** Eine *Variable* ist ein benannter Speicherplatz, der einen bestimmten Wert enthalten kann. Sie wird verwendet, um Daten zu speichern und im Programm weiterzuverarbeiten.

**Beispiele (in Python):**
```py
name = "Anna"
age = 25
money = 19.99
isaktiv = True
```


## 3. String / Zeichenketten
**Definition:** Eine *Zeichenkette (string)* ist eine Folge von *Zeichen (chars)*, die Text darstellen. Sie wird in Anführungszeichen geschrieben.

**Beispiele (in Python):**
```py
text = "Hello World"
char = "A"
empty = ""
```


## 4. Array
**Definition:** Ein *Array* ist eine *Datenstruktur*, die eine feste Anzahl von Elementen desselben Typs in einer bestimmten Reihenfolge speichert. Man kann mit einem *Index* direkt auf jedes Element zugreifen (`array[0]` für das erste Element).

**Beispiele (in Python):**
```java
int[] array = {1, 2, 3, 4, 5};
System.out.println(array[2]);
```


## 5. Schleifenarten (Loops)
**Definition:** Schleifen ermögichen es, einen Codeblock mehrfach auszuführen - entweder eine bestimmte Anzahl von Durchläufen oder solange eine Bedingung erfüllt ist.

**Arten & Besipiele:**  
**1. for-Schleife** Wird verwendet, wenn die Anzahl der Wiederholungen bekannt ist.
```py
for i range(5):
  print(i)
```

**2. while-Schleife** Wiederholt sich, solange eine Bedingung wahr ist.
```py
i = 0
while i < 5:
  print(i)
  i += 1
```

**3. do-while-Schleife (JS)** Führt den Code mindestens einmal aus, bevor die Bedingung geprüft wird.
```js
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

## 6. Abfragen (Bedingungen / If-Statements)
**Definition:** Abfragen steuern, welcher Code ausgeführt wird - basierend auf Bedingungen (zB. Vergleiche, Wahrheitswerte).

**Beispiel:**
```py
age = 18
if age >= 18:
  print("Volljährig")
else:
  print("Minderjährig")
```

## 7. Mehrfachauswahl (switch)
**Definition:** Diese Konstruktionen erlauben es, mehrere mögliche Fälle zu behandeln, ähnlich wie eine Abfolge von `if/elif/else`.

**Beispiel:**
```js
let day = 2;
switch(day) {
  case 1:
    console.log("Montag");
    break;
  case 2:
    console.log("Dienstag");
    break;
  case 3:
    console.log("Mittwoch");
    break;
}
```