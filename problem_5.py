def generateMin():
	generateNumber = 1

	thisDone = True
	while thisDone:
		counter = 0
		for num in range(1, 21):
			if generateNumber % num == 0:
				counter += 1

		if counter == 20:
			return generateNumber
		generateNumber += 1

print(generateMin())

