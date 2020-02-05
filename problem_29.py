def get_numbers(fin_number):
	mass = set()

	for num in range(2, fin_number + 1):
		for degree in range(2, fin_number + 1):
			mass.add(num ** degree)

	return len(mass)

fin_number = 100
print(get_numbers(fin_number))