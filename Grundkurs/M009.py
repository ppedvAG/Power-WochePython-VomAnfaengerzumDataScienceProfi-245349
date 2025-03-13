# Input/Output
# Konsoleneingaben vom Benutzer
# Dateien schreiben/lesen

# input
# Stellt dem User eine Frage
# Der Input des Users wird in eine Variable geschrieben
def inputDemo():
	name = input("Gib deinen Namen ein: ")
	print(f"Hallo {name}")

	x = input("Gib eine Zahl ein: ")  # x ist ein string
	x = int(x) # Wenn wir mit der Zahl rechnen wollen, müssen wir konvertieren
	print(x * 2)

#####################################################

# open
# Öffnet einen Stream zu der angegebenen externen Resource
# -> In unserem Fall zu einer Datei

file = open("Test.txt", mode="w")  # Bei open muss ein Pfad + ein Modus angegeben werden
# Wichtige Methoden:
# - read, write: Lesen/Schreiben von Daten
# - flush: Den Inhalt des Buffers in die unterliegende Datei schreiben
# - close: Schließt den Stream zur Datei, und gibt die Datei frei

file.write("Hallo Welt")  # Hallo Welt wird erstmal in den Stream geschrieben; die Datei ist noch leer
file.flush()  # Schreibt den Inhalt des Buffers in die Datei
file.close()  # Gibt die Resource (= die Datei) wieder frei

# Lesen mit open
readFile = open("Test.txt", mode="r")
zeilen = readFile.readlines()
print(zeilen)

#####################################################

# Escape-Sequenzen
# Nicht sichtbare Zeichen, die aber trotzdem in Strings eingebettet werden sollen
# https://learn.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170

# Wichtigste Escape-Sequenzen
# \n: Zeilenumbruch
# \t: Tabulator
# \\: Backslash
pfad = "C:\\Users\\lk3\\source\\repos"  # Ein einzelner Backslash in einem Pfad muss immer ein doppelter Backslash sein

s = "Hallo\nWelt"
print(s)

#####################################################

# with-Statement
# Automatisiert den open Prozess
# -> flush und close werden automatisch gemacht

with open("Test.txt", mode="w") as f:  # as f: Variablenname
	f.write("Hallo Welt")

# f = open("Test.txt", mode="w")
# f.write("Hallo Welt")
# f.flush()
# f.close()

#####################################################

# raw string
# String, welcher Escape-Sequenzen ignoriert
pfadOhneR = "C:\\Users\\lk3\\source\\repos"  # normaler Pfad ohne r
pfadR = r"C:\Users\lk3\source\repos"

sR = r"Hallo\nWelt"
print(sR)

#####################################################

# import os.path
from os.path import exists

if exists("Test.txt"):
	print("File existiert")