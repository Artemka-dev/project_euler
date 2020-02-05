def isPrimeNumber(number):
	if number < 2: return False

	counter = 0
	for num in range(1, number + 1):
		if number % num == 0: counter += 1

	if counter <= 2: return True
	else: return False

mass = []
count = 0
number = 10
while len(mass) != 11:
	numbers = [str(i) for i in str(number)]
	mass_len = len(numbers)
	for index in range(0, mass_len):
		ind_1 = int("".join(numbers[index:]))
		if index == 0:
			index = 1
			ind_2 = int("".join(numbers[:-index]))
		else:
			ind_2 = int("".join(numbers[:-index]))
		if isPrimeNumber(ind_1) and isPrimeNumber(ind_2):
			count += 1
	if count == mass_len and number % 2 != 0: 
		print(number)
		mass.append(number)
	else: count = 0
	number += 1

print(sum(mass))