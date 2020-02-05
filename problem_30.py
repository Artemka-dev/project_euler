numbers = []
for number in range(1000, 1000000):
	mass = [int(i) for i in str(number)]
	summa = 0
	for element in mass:
		summa += element ** 5
	if summa == int(number):
		numbers.append(number)

print(sum(numbers))