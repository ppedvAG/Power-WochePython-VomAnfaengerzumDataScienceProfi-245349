# Lambda

def hallo():
	print("Hallo Welt")

hallo()

# Die Funktion in Zeile 3 ist ein Objekt

h = hallo  # Speichert einen Funktionszeiger in diese Variable
print(h)

h()  # Diese Variable kann jetzt ausgeführt werden

# Anonyme Funktion (Lambda Expression)
# Methoden in Variablen speichern, ohne dedizierte Methode anzulegen
# Syntax: lambda <Par1>, <Par2>, ...: <Body>
l = lambda x, y: print(f"{x} + {y} = {x + y}")

def addiere(x, y):
	print(f"{x} + {y} = {x + y}")

# Verwendung: Funktionszeiger als Parameter bei einer anderen Funktion
def runFunc(func, x, y):
	func(x, y)

runFunc(l, 2, 3)

############################################################

# filter und map
# Diese beiden Funktionen benötigen jeweils einen Funktionszeiger/Lambda Expression

# filter
# Lässt eine Schleife über die Liste laufen, und führt bei jedem Element die Funktion aus
# Jedes Element, welches True zurückgibt, ist bei der Filterung
f = [1, 2, 3, 4, 5]
filter(lambda x: x % 2 == 0, f)  # Das Listenelement (x), die Bedingung in der Lambda Expression (x % 2 == 0), die Liste selbst (f)

print(list(filter(lambda x: x % 2 == 0, f)))

output = []
for x in f:
	if x % 2 == 0:
		output.append(x)
print(output)

print([x for x in f if x % 2 == 0])

# map
# Transformiert die Liste
# Führt bei jedem Listenelement eine Funktion aus, und nimmt die Rückgabewerte der Funktion als die Ergebnismenge
m = [1, 2, 3, 4, 5]

map(lambda x: x ** 2, m)

print(list(map(lambda x: x ** 2, m)))