# List
# Typ, welcher mehrere Werte halten kann
# Die Inhalte können sich von Typen her mischen
# Duplikate sind auch möglich
# Index ist auch möglich

# Definition
l = [1, 2, 3, "Hallo"]  # Liste definieren mit []
print(l)

# Index
print(l[0])
print(l[-1])
print(l[1:3])

# Länge der Liste
print(len(l))

# Listenfunktionen
# list.append(Wert): Neues Element hinzufügen
l.append(5)
print(l)

# list.remove(Wert): Sucht nach dem gegebenen Wert, und entfernt das erste Vorkommnis
l.remove("Hallo")
print(l)

# list.sort(): Sortiert die Liste
l.sort()
l.sort(reverse=True)  # Absteigend sortieren
print(l)

# list.extend(Andere Liste): Baut zwei Listen zusammen
# Problem: Mit append wird die neue Liste als ein einzelnes Element hinzugefügt
n = [4, 5, 6]
l.append(n)
print(l)  # Verschachtelte Liste

l.remove(n)
l.extend(n)
print(l)  # Einzelne Liste

# Mit += kann auch ein extend erzielt werden
l += n
print(l)

######################################################################

# Tuple
# Funktioniert wie eine Liste, aber es kann nicht verändert werden
t = (1, 2, 3)  # Runde Klammern statt eckigen Klammern
print(t)

# Index
print(t[0])

# Tupel verändern
# Über Umweg (Konvertierung)
x = list(t)
x.append(4)
t = tuple(x)
print(t)

# Konvertierungen
# Variablen von einem Typen zu einem anderen Typen konvertieren
# Syntax: <Zieltyp>(<Variable>)
# z.B.: list <-> tuple

# Beispiel: str -> int
eingabe = "50"
eingabe = int(eingabe)  # Wenn keine Konvertierung stattfindet: 50 * 2 = 5050
print(eingabe * 2)

# Beispiele: Kommastellen abschneiden
f = 24.23
print(int(f))

# Unpacking
# Listentypen zu einzelnen Variablen zerlegen
# Beispiel: t zu 4 einzelnen Variablen zerlegen
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)

######################################################################

# range
# Generator für Zahlen von X bis Y
# Syntax: range(Untergrenze, Obergrenze, Schrittgröße)
r = range(100)  # Zahlen von 0-99

r2 = range(50, 100)  # Zahlen von 50-99

r3 = range(50, 100, 5)  # 50, 55, 60, 65, 70, ...

# WICHTIG: Range ist nur ein Generator
print(r)  # Keine Werte

print(list(r))  # Generator "ausführen"
print(tuple(r))

######################################################################

# set
# Funktioniert wie eine Liste, aber kann keine Duplikate enthalten
s = {1, 2, 3, 4, 5}
print(s)

# Wenn ein Wert hinzugefügt wird, welcher bereits existert, passiert nichts
s.add(1)
print(s)

# Beispiel: Liste deduplizieren
ls = set(l)
print(list(ls))

######################################################################

# dict
# Liste mit BENANNTEN Werte
# Jeder Wert in einem Dictionary muss einen Schlüssel haben

# person = ["Lukas", 26, 75]  # Nicht Aussagekräftig
person = {
	"Vorname": "Lukas",
	"Alter": 26,
	"Gewicht": 75,
	"Koerpergroesse": 178,
	"ArbeitswegKM": 12
}

# Verwendung: Werten eine Bezeichnung geben

# Index
# Der Index ist hier ein String-basierter Index
print(person["Vorname"])  # Wert hinter dem Feld angreifen

# Inhalte des dicts ausgeben
print(person.keys())
print(person.values())
print(person.items())

# Neue Felder hinzufügen
person["Wegzeit"] = 40  # Mit = können Werte geschrieben/verändert werden

print(person)