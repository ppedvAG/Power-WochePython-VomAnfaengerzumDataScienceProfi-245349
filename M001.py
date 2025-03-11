list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8, 9]

laengen = [len(list1), len(list2), len(list3)]
laengen.sort()
laengste = laengen[-1]

if len(list1) == laengste:
	print("list1 ist die längste Liste")
if len(list2) == laengste:
	print("list2 ist die längste Liste")
if len(list3) == laengste:
	print("list3 ist die längste Liste")

##################

list4 = list1 + list2 + list3
if 3 in list4 or 7 in list4 or 10 in list4:
	print()

print({3, 7, 10}.intersection(list4))

##################

for i in range(1, 200):
	s = str(i)
	if i % 100 in [11, 12, 13]:
		print(f"{i}th")
	elif s[-1] == "1":
		print(f"{i}st")
	elif i % 10 == 2:
		print(f"{i}nd")
	elif i % 10 == 3:
		print(f"{i}rd")
	else:
		print(f"{i}th")

##################

text = "Ich bin ein Text"
split = text.split(" ")
print(split)