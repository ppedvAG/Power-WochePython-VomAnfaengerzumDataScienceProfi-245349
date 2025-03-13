# Kommentare
# Text, welcher vom Interpreter ignoriert wird
# Wird mit einer Raute (#) angegeben
print(5)  # Kann auch innerhalb einer Zeile existieren

######################################################################

# Variable
# Feld, welches einen Wert halten kann
# Werden in der Programmierung immer benötigt
# Syntax: <Name> = <Wert>
x = 5  # Ab hier kann die Variable x ausgelesen werden
print(x)  # Ruft den Inhalt von x ab, und schreibt diesen Konsole

# Der Typ einer Variable wird über den Inhalt dieser Variable festgelegt
# x = 5 -> x ist vom Typ int
x = "Hallo"
# x = "Hallo" -> x ist vom Typ string

# Typen in Python
# int: Ganze Zahl
y = 4273684789764932091876902483675927649347493274365  # int kann in Python beliebig klein/groß sein
print(type(y))

# float: Kommazahl
z = 21874971280947124832587691248.3517862379582196742957249
print(type(z))

# str: String (Text)
s1 = "Hallo Welt"
s2 = 'Hallo Welt'  # Einzelne Hochkomma sind auch möglich (kein Unterschied)
print(type(s1))

# bool: Wahr-/Falschwert (True oder False)
w = True
f = False
print(type(w))

# complex: Komplexe Zahlen
c = 12 + 5j  # Der imaginäre Teil wird als j bezeichnet
print(type(c))

######################################################################

# Stringfunktionen
text = "Das Ist Ein Text"

# Punkt-Operator: In die Variable hineingreifen
print(text.isalnum())
print(text.isalpha())
print(text.isnumeric())

print(text.lower())
print(text.upper())

print(text.count("e"))  # Wie oft ist ein "e" enthalten

# Wieviele "e" und "E" haben wir?
print(text.count("e") + text.count("E"))

print(text.lower().count("e"))  # Funktionen verketten, die count Funktion verwendet das Ergebnis von lower()

# Wie lang ist der Text?
print(len(text))  # 16

######################################################################

# Index
# Bestimmte Stellen einer Liste angreifen
# Funktioniert auch bei einem String
print(text[0])  # Einzelnes Element entnehmen (Element 0)

print(text[-1])  # String von rechts angreifen (-1: das letzte Zeichen)

print(text[0:3])  # Bereich nehmen (von 0 bis exklusive 3) -> 0, 1, 2

print(text[0:-1])  # Von 0 bis zum VORLETZTEN Zeichen (weil Obergrenze exklusiv)

print(text[0:])  # Bei einem Bereich können auch Grenzen weggelassen werden

print(text[:3])  # Vom Anfang bis Stelle 3

print(text[:])  # Beide Grenzen weglassen

######################################################################

# Arithmetik
# Matematische Operatoren
z1 = 7
z2 = 4

# Unterschied zw. + und +=
z1 + z2  # Summe wird berechnet, z1 und z2 bleiben unverändert
print(z1)  # 7
print(z2)  # 4

z1 += z2  # Bildet die Summe, und schreibt diese in z1 (addiere z2 auf z1)
print(z1)
print(z2)

# Nur die Summe berechnen
print(z1 + z2)
# += nur verwenden, wenn sich eine der Variablen ändern soll
# + in allen anderen Fällen benutzen

# **: Potenz Operator (x^...)
print(3**3)  # 3^3=27

print(9**(1/2))  # Wurzel ziehen mit Potenzoperator

# Divisionen
# Hauptregel: Eine Division gibt immer eine Kommazahl
print(9 / 2)  # 4.5

# //: Ganzzahldivision
print(9 // 2)  # 4

# Modulo-Operator (%): Rest einer Division
print(9 % 2)  # 1
# 9 / 2 = 4
# 1R.

# Arithmetik mit Strings
hallo = "Hallo"
welt = "Welt"
print(hallo + welt)

# Strings multiplizieren
print(hallo * 10)