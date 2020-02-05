NUMBER = 1000000

startNumber = NUMBER
num = NUMBER
startMassive = []
counter = 0
finMassive_1 = []
finMassive_2 = []
while counter != NUMBER:
	startMassive = []
	while startNumber != 1:
		startMassive.append(startNumber)
		if startNumber % 2 == 0: startNumber = int(startNumber / 2)
		else: startNumber = int(startNumber * 3 + 1)

	counter += 1
	finMassive_1.append(num)
	finMassive_2.append(len(startMassive))
	num -= 1; startNumber = num

dictionary = dict(zip(finMassive_1, finMassive_2))
max_value = max(dictionary.values())
final_dict = {k:v for k, v in dictionary.items() if v == max_value}

print(final_dict)

