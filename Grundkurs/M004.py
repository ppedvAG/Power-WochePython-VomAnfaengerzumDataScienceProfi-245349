# Abfragen
# Mithilfe von if-Bedingungen können bestimmte Codeteile übersprungen werden

# if-Bedingung
a = 1
if a < 10:  # Wenn a kleiner als 10 ist, wird der gesamte Code innerhalb der if ausgeführt
	print("a ist kleiner als 10")  # WICHTIG: Einrückungen beachten
print("Nach der if")  # Ohne Einrückung gehört diese Codezeile nicht mehr zur if dazu

# else-Bedingung
# Wird nur ausgeführt, wenn die if nicht ausgeführt wird
# Es wird immer entweder if oder else ausgeführt, aber nie beide
if a < 10:
	print("a ist kleiner als 10")
else:  # Gegenteil der if-Bedingung
	print("a ist größer oder gleich 10")

# elif-Bedingung
# Eine else-Bedingung, mit einer zusätzlich Bedingung
if a < 10:  # -∞ bis 9
	print("a ist kleiner als 10")
elif a > 10:  # 11 bis ∞
	print("a ist größer als 10")
else:  # genau 10
	print("a ist 10")

######################################################################

# Vergleichsoperatoren
# Benötigen zwei Werte, diese werden verglichen
# ==, !=, <>: gleich, ungleich
# <, >=: kleiner, größer-gleich
# >, <=: größer, kleiner-gleich

# Logische Operatoren
# and, or: und, oder

# Und/oder werden verwendet, um zwei Bedingungen zu verknüpfen
b = 0
c = 3
if b < 10 and b != c:  # and: Beide Bedingungen müssen wahr (True) sein
	print("b kleiner 10 und b nicht c")

if b < 10 or b != c:  # or: Eine der beiden Bedingungen (oder beide) müssen wahr (True) sein
	print("b kleiner 10 oder b nicht c")

# if auswerten
if b < 10 or b != c:
	print()

if True or True:  # Jeder Teil wird zu True/False umgewandelt
	print()

if True:  # Wenn am Ende der Simplifizierung nurnoch einmal True hier steht, wird der Code ausgeführt
	print()

# Not: Kehrt eine Bedingung um
if not b < 10:
	print("")

if b >= 10:  # Vereinfachung von dem Beispiel darüber
	print("")

# In: Prüft, ob ein Wert in einer Liste enthalten ist
l = [1, 2, 3]
if a in l:
	print("Der Wert hinter a (" + str(a) + ") ist in l enthalten")

# Hier ist not manchmal notwendig
if a not in l:
	print("a ist nicht in l enthalten")

text = "Hallo Welt"
if "a" in text:
	print("text enthält ein a")

# Is: Prüft, ob zwei Objekte die selbe Speicheradresse haben
if a is 1:
	print("a ist 1")

######################################################################

# Ternary-Operator: Kurzschreibweise von if-elif-else Blöcken
if a < 10:  # -∞ bis 9
	print("a ist kleiner als 10")
elif a > 10:  # 11 bis ∞
	print("a ist größer als 10")
else:  # genau 10
	print("a ist 10")

print("a ist kleiner als 10") if a < 10 else print("a ist größer als 10") if a > 10 else print("a ist 10")
print("a ist kleiner als 10" if a < 10 else "a ist größer als 10" if a > 10 else "a ist 10")