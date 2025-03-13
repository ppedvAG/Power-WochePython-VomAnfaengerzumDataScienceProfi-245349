# Decorator
# Vor/Nach einer Funktion beliebigen Code ausführen
# Wrapper für eine Funktion

def testDecorator(func):
	def wrapper():
		print("Vor der Funktion")
		func()  # Die Funktion, die decorated wird, wird hier ausgeführt
		print("Nach der Funktion")
	return wrapper


@testDecorator  # Funktion verändern, ohne die Funktion selbst zu verändern
def hallo():
	print("Hallo Welt")

hallo()  # Jetzt wird im Hintergrund die wrapper() Funktion des testDecorators ausgeführt

################################################

# Eigener Decorator
# Zeitmesser
def measureTime(func):
	import time
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(f"{round(end - start, 2)}s")
	return wrapper

@measureTime
def generateNumbers(amount: int):
	x = list(range(amount))

generateNumbers(100_000_000)