import sqlite3

def createPersonenTable():
	cursor.execute("CREATE TABLE Personen(id int, vorname varchar(20), nachname varchar(20))")
	connection.commit()


def insertData():
	cursor.execute("INSERT INTO Personen VALUES (0, 'Lukas', 'Kern')")
	cursor.execute("INSERT INTO Personen VALUES (1, 'Matthias', 'Kaiser')")
	cursor.execute("INSERT INTO Personen VALUES (2, 'Dominik', 'Enzenhofer')")
	connection.commit()

# Model Klasse
# Klasse, welche eine Datenbanktabelle repräsentiert
# Jeder Datensatz wird zu einem Objekt in der Applikation
# Model Klassen automatisieren: SQLAlchemy
class Person:
	def __init__(self, id, vorname, nachname):
		self.id = id
		self.vorname = vorname
		self.nachname = nachname


with sqlite3.connect("Test.db") as connection:
	# Cursor erstellen, um mit Tabellen zu interagieren
	cursor = connection.cursor()

	# DB zurücksetzen
	cursor.execute("DELETE FROM Personen")
	insertData()

	# Daten laden
	data = cursor.execute("SELECT * FROM Personen").fetchall()

	personen = []
	for p in data:
		personen.append(Person(p[0], p[1], p[2]))

	# Alle Vornamen ausgeben
	for x in data:
		print(x[1])

	for y in personen:
		print(y.vorname)