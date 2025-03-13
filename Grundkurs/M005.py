# Schleifen
# Ein Stück Code mehrmals ausführen
# Eine Schleife besteht immer aus dem Keyword selbst (while/for) und eine Bedingung oder eine Liste

# while
# Führt den Code solange aus, wie die gegebene Bedingung True ist
a = 0
while a < 10:  # Solange a kleiner als b ist
	print(a)
	a += 1
# Wenn die Schleife zu Ende ist, springe zum Schleifenkopf zurück

# break und continue
# break: Beendet die Schleife, der Code läuft nach der Schleife weiter
b = 0
while b < 20:
	print(b)
	b += 1

	if b == 15:
		break  # Wenn b 15 ist, wird die Schleife beendet
print("Nach der Schleife")  # Schleife wird vorzeitig abgebrochen

# continue: Überspringe ab hier den Rest der Schleife, und gehe zum Anfang zurück
c = 0
while c < 10:
	c += 1
	if c == 5:
		continue  # Wenn c 5 ist, wird das print übersprungen
	print(c)

# Endlosschleife
# "Tu etwas, bis zu einem bestimmten Zeitpunkt"
# Wird generell mit einer if + break beendet
e = 0
while True:
	print(e)
	e += 1

	if e == 100:
		break

# Aufgabe: Liste ausgeben mit einer while-Schleife
zahlen = [3, 1, 8, 29, 58, 19, 20, 33, 58, 19, 28, 4, 1, 9]

z = 0
while z < len(zahlen):
	print(zahlen[z])
	z += 1

# Aufgabe: Text rückwärts anzeigen
text = "Hallo Welt"
q = len(text) - 1
while q >= 0:
	print(text[q])
	q -= 1

# Aufgabe: Zweipotenzen anzeigen
# 2, 4, 8, 16, 32, 64, ...
p = 1
while p < 50:
	print(2 ** p)
	p += 1

p = 2
while p < 100000:
	print(p)
	p *= 2

######################################################################

# for-Schleife
# Schleife, welche IMMER über eine Liste geht
# z.B.: List, Tuple, Range, Set, Dict, String, ...
# Syntax: for <Variablenname> in <Liste>:
l = [2, 6, 8, 3, 1]
for zahl in l:  # zahl stellt einen Zeiger dar, welcher immer auf ein Listenelement zeigt
	print(zahl)
# Am Ende der Schleife, wird der Zeiger um ein Element weiterbewegt

# while und for Vergleich

# Aufgabe: Alle Zahlen von 0 bis 9 ausgeben

print("while: ")
w = 0
while w < 10:
	print(w)
	w += 1

print("for: ")
for i in range(10):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(i)

# Aufgabe: Liste ausgeben mit einer for-Schleife
zahlen2 = [3, 1, 8, 29, 58, 19, 20, 33, 58, 19, 28, 4, 1, 9]

# z = 0
# while z < len(zahlen):
# 	print(zahlen[z])
# 	z += 1

for r in zahlen2:
	print(r)

# Aufgabe: Text rückwärts anzeigen
text = "Hallo Welt"
# q = len(text) - 1
# while q >= 0:
# 	print(text[q])
# 	q -= 1

for g in text[::-1]:
	print(g)

# Aufgabe: Zweipotenzen anzeigen
# 2, 4, 8, 16, 32, 64, ...

# p = 1
# while p < 50:
# 	print(2 ** p)
# 	p += 1

# p = 2
# while p < 100000:
# 	print(p)
# 	p *= 2

for k in range(1, 20):
	print(2 ** k)

######################################################################

# Verschachtelte Schleifen
# Schleife in einer anderen Schleife
# Für jeden Durchlauf der äußeren Schleife, wird die innere Schleife komplett ausführt
summe = 0
for x in range(5):  # Für jede Ausführung der äußeren Schleife, wird die innere Schleife 5 mal ausgeführt
	for y in range(5):  # 5 Ausführungen
		summe += 1
print(summe)

######################################################################

# fstring
# Formatted String
# Code in einen String einbetten

# print("Hallo " + 5)  # Fehler
print("Hallo " + str(5))  # Kein Fehler mit Konvertierung
print(f"Hallo {5}")

# Mithilfe von { } kann jetzt Code in den String eingebettet werden
for i in range(1, 11):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl hoch 2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))
	print("--------------------------------")

	# Konvertierung wird hier automatisch gemacht
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl hoch 2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")
	print("--------------------------------")