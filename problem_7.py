def generatorNumbers():
	count = 0
	num = 2
	massNumbers = []
	while len(massNumbers) != 10002:
		count = 0
		for number in range(1, num + 1):
			if num % number == 0:
				count += 1

		if count <= 2: massNumbers.append(num)
		num += 1

	return massNumbers[10001]

print(generatorNumbers()) # 10743