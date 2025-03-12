# Fehlerbehandlung

# x = input("Gib eine Zahl ein: ")
# zahl = int(x)  # Wenn hier keine Zahl eingegeben wird, stürzt das Programm ab. Warum?

def zahlEingabeIf():
	x = input("Gib eine Zahl ein: ")
	if x.isnumeric():
		zahl = int(x)
	else:
		# Statt eines Absturzes, können wir im else-Block eine Fehlerbehandlung durchführen
		print("Keine Zahl eingegeben")
		# logger.log("Keine Zahl eingegeben")  # Statt der Konsole kann die Fehlermeldung auch in einem Log/einer GUI/einer Webseite/einer DB ausgegeben werden

# Manchmal können Fehler mit einer einfach if-Bedingung verhindert werden
# Wenn dies aber nicht möglich ist, muss stattdessen die try-except Mechanik verwendet werden
# Beispiel: Webschnittstelle
# - Wenn wir uns zu einer Webschnittstelle verbinden wollen, müssen wir eine Verbindung herstellen
# - Wenn aber die URL einen Tippfehler hat, kann dies nicht mit einer if im vorhinein verhindert werden
# - Dieser Fehler wird dem User als eine Exception (= Ausnahme) vermittelt

# try-except
# Wenn ein Absturz passieren würde, kann dieser mit try-except verhindert werden
# Wenn ein Fehler auftritt, wird der except-Block ausgeführt

# Annahme: Konvertierung von str zu int kann nicht per if verhindert werden
try:
	x = input("Gib eine Zahl ein: ")
	zahl = int(x)
	print(10 / zahl)
except ValueError:
	print("Keine Zahl eingegeben")
except ZeroDivisionError as e:
	print("Division durch 0 nicht möglich")

	# Traceback
	# Informationen für Entwickler, wo der Fehler aufgetreten (Python Skript + Zeilennummer)
	from traceback import format_exception
	for line in format_exception(e):
		print(line)
except:
	print("Anderer Fehler")
else:  # else: Wenn der try-Block ohne Fehler abgelaufen ist
	print()
finally:  # finally: Wird immer ausgeführt (ob Fehler oder nicht)
	print()


# Der except-Block
# Drei Varianten:
# except <Fehler>: Dieser Block behandelt nur diesen spezifischen Fehler
# except <Fehler> as <Name>: Dieser Block behandelt nur diesen spezifischen Fehler, über den Namen können zusätzliche Informationen über den Fehler erlangt werden
# except: Dieser Block behandelt alle Fehler


# raise
# Das Programm abstürzen lassen
# Syntax: raise <Fehlertyp>
raise SystemError("Das Programm stürzt hier ab")