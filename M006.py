# List Comprehension
# Schnelle Syntax um Listen zu erstellen

zahlen = []
for i in range(1, 11):
	zahlen.append(i)
print(zahlen)

# LC
zahlenLC = [i for i in range(1, 11)]
print(zahlenLC)

print([i for i in range(1, 11)])

##############################################

# if-Anweisungen mit LC
# Mit einer if-Anweisung kann die Anzahl der Werte reduziert werden

# Aufgabe: Nur Zahlen inkludieren in der Form x^2
hoch2 = []
for i in range(100):
	hoch2.append(i ** 2)

iHoch2 = []
for i in range(100):
	if i in hoch2:
		iHoch2.append(i)
print(iHoch2)

# LC
print([i for i in range(100) if i in hoch2])

##############################################

# Linke Seite anpassen
# Werte verändern, bevor diese in die Liste geschrieben werden
hoch2Strings = []
for i in range(50):
	hoch2Strings.append(f"{i}^2={i ** 2}")
print(hoch2Strings)

# LC
print([f"{i}^2={i ** 2}" for i in range(50)])

##############################################

# Verschachtelte Schleifen
einsMalEins = []
for x in range(1, 11):
	for y in range(1, 11):
		einsMalEins.append(f"{x}*{y}={x * y}")
print(einsMalEins)

# LC
print([f"{x}*{y}={x * y}" for x in range(1, 11) for y in range(1, 11)])

##############################################

# Ternary Operator
for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)

# LC
print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)])