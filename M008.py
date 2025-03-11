# Module
# Größe Python Code Ansammlungen in mehrere Skripte aufteilen, und diese aufeinander referenzieren

# Module importieren
# Zwei Optionen
# - import
# - from import
# Module können auch mit einem Alias versehen mit (as <Name>)

# import
# Importiert alle Variablen, Funktionen und Klassen aus dem anderen Skript
import M001
M001.countCase("Das ist ein längerer Text")

# Wenn ein Skript importiert wird (mit import oder from import), wird immer das gesamte File ausgeführt
# -> Wenn ein neues Skript erstellt wird, sollte jeglicher Code in einer Funktion/Klasse sein

# from import
# Importiert nur bestimmte Variablen/Funktion/Klassen
# Syntax: from <Skript> import <Member1>, <Member2>, ...
from M007 import hallo, summiere, summe
hallo("Lukas")  # Vorteil: Skriptname kann hier nicht angegeben werden
summiere(1, 2, 3)
summe(1, 2)

# Alias
# Mit einem Alias kann ein Import umbenannt werden
# Syntax: as <Name>
import M006 as m
print(m.zahlen)

# Import *
# Importiert alles aus dem Skript
# Nur beim from-Import möglich
from M006 import *

###################################################################

# Modul Suchpfade
# Wenn das Import Keyword verwendet wird, muss das Skript gesucht werden
# Die durchsuchten Pfade sind in sys.path gespeichert
import sys
for p in sys.path:
	print(p)

# Drei Pfade:
# - Der Pfad des Skriptes selbst (+ Unterpfade)
# - Der Pfad der Python Standardinstallation
# - Der Pfad der .venv des Projekts (selbst installierte Pakete)
# Wenn das Skript nicht gefunden wird -> ModuleNotFoundError

# Zusätzliche Pfade können an sys.path angehängt werden
sys.path.append("C:\\Users\\lk3\\Desktop")

# import xyz

###################################################################

# Externe Pakete installieren
# Wenn ein externes Paket installiert wird, wird dieses immer in der .venv gespeichert
# .venv/Lib/site-packages

# Zwei Optionen für Installation:
# - PyCharm: Python Packages
# - Terminal (PowerShell/Bash)
# -- pip install <Name>

import numpy as np
r = np.round(3.4568284912793, decimals=3)
print(r)

###################################################################

# Die Main Methode
# Der Startpunkt des Programms
# Wird immer am Ende des Skripts platziert
# Besteht immer aus einer if

# __name__
# 1. Der Name des Skripts, wenn es importiert wurde
# 2. __main__ wenn das Skript direkt gestartet wurde
print(__name__)

# import M008_Package.Test

def main():
	print()

if __name__ == "__main__":
	main()

###################################################################

# Packages
# Ordner, um die Projektstruktur nochmal zu verbessern
# Müssen beim Import mitangegeben werden

# __init__.py
# Kann Standardcode enthalten, welcher immer ausgeführt wird, wenn das Paket angegriffen wird
import M008_Package.Test

# Alle Skripte gleichzeitig aus dem Package importieren
from M008_Package import *