def summaSimpleNumbers():
	count = 0
	massNumbers = []
	num = 2
	while num <= 10:
		count = 0
		for number in range(1, num + 1):
			if num % number == 0:
				count += 1

		if count <= 2: massNumbers.append(num)
		num += 1

	return sum(massNumbers)

print(summaSimpleNumbers())