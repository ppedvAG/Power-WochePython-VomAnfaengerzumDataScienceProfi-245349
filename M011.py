# Vererbung
# Definition von Oberklassen und Unterklassen
# Jede Oberklasse hat bestimmte Felder/Funktionen
# Jeder Unterklasse erbt die Felder/Funktionen von ihrer Oberklasse
# Hintergrund: Generalisierung, allgemeine Basis, leichte Anpassungen in den Unterklassen

# Beispiel: object
# Object ist die Basisklasse von allen Klassen in Python
# Die object Klasse vererbt viele Funktionen an alle Klassen
# - __init__, __str__, ...

# Eigene Vererbungshierarchie
# Oberklasse: Lebewesen
# - Feld: Alter
# - Funktion: Bewegen
# Unterklassen: Mensch, Hund
# - Mensch: Name, Sprechen
# - Hund: Fellfarbe

class Lebewesen:
	def __init__(self, alter: int):
		self.alter = alter

	def bewegen(self, distanz: int):
		print(f"Das Lebewesen bewegt sich um {distanz}m")


class Mensch(Lebewesen):
	"""
	Über den Klassennamen in der Klammer wird eine Vererbung hergestellt
	"""

	def __init__(self, alter: int, name: str):
		"""
		Call to __init__ of super class is missed

		Wenn __init__ in einem Vererbungskontext verwendet wird, muss immer eine Verkettung gemacht werden
		"""
		super().__init__(alter)
		self.name = name

	def sprechen(self, text: str):
		print(f"{self.name} sagt: {text}")

	def __str__(self):
		s = super().__str__()  # <__main__.Lebewesen object at 0x000001615B527E00>
		return f"Der Mensch {self.name} ist {self.alter} Jahre alt. ({s})"

class Hund(Lebewesen):
	pass  # pass: Platzhalter für einen leeren Codeblock

m = Mensch(20, "Max")
m.bewegen(10)
m.sprechen("Hallo")

####################################################

# Vererbung durch object
# Die object Klasse vererbt viele Methoden an alle Klassen in Python
# __init__: Initialmethode
# __str__: ToString, erzeugt eine String-Repräsentation des Objekts
# __str__ wird häufig überschrieben, um das Standardverhalten zu verändern (<__main__.Mensch object at 0x000001D6AC387CB0>)
print(m)

l = Lebewesen(10)
print(l)