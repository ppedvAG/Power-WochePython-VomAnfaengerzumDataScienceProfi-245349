# Klassen und Objekte

# Klasse
# - Bauplan des Objekts; in der Klasse werden Felder und Funktion definiert, welche alle Objekte besitzen
# - Aus dem Bauplan werden im Anschluss beliebig viele Objekte erstellt
# - Zwei Typen von Klassen: Funktionsklassen und Datenklassen
# -- Funktionsklasse: Klasse, welche etwas tun soll
# -- Datenklasse: Klasse, welche einfach nur Daten halten soll (kaum/keine Funktionen)

# Beispiele:
# - int: Datenklasse
# - str: Funktions- und Datenklasse
# - list: Datenklasse
# - TextIO (open): Funktionsklasse

# Wir können eigene Klassen definieren, um selbst Funktions-/Datenklassen zu definieren
# Datenklassen können erzeugt werden, um komplexe Zustände darzustellen

# int: ganze Zahl
# float: Kommazahl
# str: Text
# list: Aufzählung
# Person: ?

#############################################################

# Die Person Klasse
# Felder
# - Vorname
# - Nachname
# - Alter
# - Gewicht
# - ...

# Funktionen
# - Sprechen
# - ...

class Person:
	"""
	docstring: Dient zum Beschreiben von Klassen/Funktionen

	Wird mit drei Hochkomma (\""") definiert unter dem Namen der Klasse/Funktion
	"""

	# Konstruktor
	# Startpunkt des Objekts
	# Wenn ein Objekt erstellt wird, wird diese Funktion ausgeführt
	# Wenn die Klasse Felder bekommen soll, müssen diese in __init__ definiert werden
	# Im __init__ werden auch konkrete Werte bei Objekterstellung empfangen

	# Felder definieren:
	# - Parameter hinzufügen
	# - self.<Feld> = <Parameter>
	def __init__(self, vorname: str, nachname: str, alter: int, gewicht: float):
		self.vorname = vorname  # self: Gibt Zugriff auf das Objekt selbst
		self.nachname = nachname
		self.alter = alter
		self.gewicht = gewicht

	# Methode
	# Wird an jedes Person Objekt angehängt
	# Wenn diese Funktion verwendet werden soll, wird ein Objekt benötigt
	# Wenn kein Objekt von der Klasse existiert, kann die Funktion nicht verwendet werden
	def sprechen(self, text: str):
		"""
		Erlaubt der Person, einen beliebigen Text zu sprechen. Beim Sprechen wird der volle Name der Person ausgegeben.

		:param text: Der Text, der von der Person gesprochen werden soll
		:return: Kein Rückgabewert
		"""
		print(f"{self.vorname} {self.nachname} sagt: {text}")

# Objekt
# Instanz von der Klasse
# In der Klasse werden nur Definitionen gemacht (Felder/Funktion erstellen)
# Im Objekt werden dann diese Felder mit konkreten Werten befüllt
# Wenn Objekte aus einer Klasse erzeugt werden, haben diese Objekte die konkrete Struktur, die in der Klasse definiert ist
# Wenn ein Objekt aus einer Klasse erstellt wird, muss es konkrete Werte erhalten

# Objekt erzeugen
p = Person("Lukas", "Kern", 26, 75)  # Hier werden konkrete Werte eingetragen

# Objekt angreifen
print(f"Die Person {p.vorname} {p.nachname} ist {p.alter} Jahre alt, und wiegt {p.gewicht}kg.")

# Funktionen im Objekt
p.sprechen("Hallo")