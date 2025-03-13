# Funktionen
# Code abspeichern, und diesen später wiederverwenden über den Namen der Funktion
# Funktionen können Daten empfangen (Parameter)
# Funktionen können Werte zurückgeben (Rückgabewerte)

# Funktionen werden mit def definiert
# Syntax: def <Name>(<Par1>, <Par2>, ...):
# 			  <Body>

def hallo():
	print("Hallo Welt")

# Ab Zeile 12 kann jetzt diese Funktion verwendet werden
hallo()
hallo()
hallo()  # Der Code in der Funktion kann jetzt beliebig oft verwendet werden

##############################################

# Funktionen mit Parameter
# Wenn eine Funktion Daten empfangen soll, müssen Parameter definiert werden
def addiere(x, y):
	print(f"{x} + {y} = {x + y}")  # x und y können hier verwendet werden

addiere(3, 4)  # Zwei ints möglich
addiere(4.3, 9.3)  # Zwei floats möglich
addiere("Hallo", "Welt")  # Zwei strings möglich

# addiere("Hallo", 123)  # Fehler, sollte nicht möglich sein

# Typen empfehlen
# Bei Parametern kann angegeben werden, welchen Typen diese haben sollten
def addiere2(x: int, y: int):
	print(f"{x} + {y} = {x + y}")

addiere2(3, 4)
addiere2(4.3, 5.2)  # Expected type 'int', got 'float' instead
addiere2(4.3, 5.2)  # Wird trotzdem ausgeführt

def addiere3(x: int | float, y: int | float): # Mehrere Empfehlungen pro Parameter mit | (oder)
	print(f"{x} + {y} = {x + y}")

addiere3(3, 4)
addiere3(8.5, 2.1)
addiere3(5.3, 2)

# Fehler verursachen, wenn die Parameter den falschen Typen haben
def addiere4(x: int | float, y: int | float):
	# Typüberprüfung
	if type(x) in [int, float] and type(y) in [int, float]:
		print(f"{x} + {y} = {x + y}")
	else:
		print("Fehler bei der Eingabe")

addiere4("Hallo", "Welt")

##############################################

# Funktionen mit Rückgabewerten
# Funktionen, welche am Ende des Codes ein Ergebnis produzieren und zurückgeben (mittels return)
# Dieses Ergebnis kann im Anschluss in einer anderen Funktion verwendet werden, oder in eine Variable geschrieben werden

def summe(x, y):
	return x + y

s = summe(3, 4)  # Ergebnis von summe wird jetzt in s gespeichert
print(s)

# Typ empfehlen
# Wie bei Parametern
def summe2(x, y) -> int:
	return x + y

s2 = summe2("Hallo", "Welt")  # Empfehlung int, eigentlicher Typ: string
print(s2)

def summe3(x: int | float, y: int | float):  # Hier wird automatisch erkannt, was der Rückgabetyp ist
	return x + y

##############################################

# Standardwerte für Parameter
# Parameter können eine Standardbelegung haben
# Dieser Parameter kann gesetzt werden, muss aber nicht gesetzt werden
# Wenn der Parameter vom Benutzer gesetzt wird, wird der Standardwert überschrieben

def hallo(name=""):
	print(f"Hallo {name}")

hallo("Lukas")
hallo()

# In anderen Sprachen gibt es ein Feature namens Überladung von Methoden
# -> Es können mehrere Funktionen definiert werden, welche den gleichen Namen haben
# In Python ist das nicht möglich

# Um in Python auch Überladung zu haben, werden optionale Parameter verwendet
# Beispiel: pandas.read_csv(...)
# read_csv hat 30+ Parameter, es muss nur ein Parameter gesetzt werden, der Rest ist optional
# Die optionalen Parameter können überschrieben werden, falls notwendig
def read_csv(path: str, delimiter: str = ",", header: bool = True):
	print("...")

read_csv("Test.csv")
read_csv("Test.csv", delimiter=";")
read_csv("Test.csv", header=False)
read_csv("Test.csv", delimiter=";", header=False)

##############################################

# Arbitrary Arguments
# Parameter, welcher beliebig viele Werte empfangen kann
# Wird mit einem Stern (*) definiert
# Kann nur einmal pro Funktion definiert werden

def summiere(*zahlen: int | float):
	# Innerhalb der Funktion wird der Parameter als ein Tuple definiert
	print(f"Summe: {sum(zahlen)}")

summiere(1, 2, 3)
summiere(1, 2, 3, 4, 5, 6, 7)
summiere(1, 2)
summiere(1)
summiere()  # Keine Parameter sind auch beliebig viele Parameter

# Unpacking
# Was ist, wenn wir eine Liste bei *args übergeben wollen?
z = (3, 1, 9, 5)
# summiere(z)  # Fehler

# Hier kann der Unpacking Operator verwendet werden
summiere(*z)  # Mit *z wird z in einzelne Zahlen zerlegt

##############################################

# Arbitrary Keyword Arguments
# Funktioniert wie *args, aber jeder Parameter MUSS einen Namen haben
def printTeilnehmer(**tn):
	for t, name in tn.items():  # tn ist hier kein Tupel, sondern ein Dictionary
		# In Python kann in einer Schleife der Wert zerlegt werden
		# t: Schlüssel (Trainer, T1, T2)
		# name: Wert ("Lukas", "Matthias", "Dominik")
		print(f"{t}: {name}")

# printTeilnehmer("Lukas", "Matthias", "Dominik")  # Nicht möglich, weil jeder Parameter einen Namen haben muss
printTeilnehmer(Trainer="Lukas", T1="Matthias", T2="Dominik")

# Unpacking
person = {
	"Vorname": "Lukas",
	"Alter": 26,
	"Gewicht": 75,
	"Koerpergroesse": 178,
	"ArbeitswegKM": 12
}

printTeilnehmer(**person)  # Funktioniert wie oben, aber benötigt 2 Sterne (**)

##############################################