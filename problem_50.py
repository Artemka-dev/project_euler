def sequence(number, prime_numbers):
	summa = 0
	for element in prime_numbers:
		summa += element
		if summa == number:
			return True, prime_numbers.index(element) + 1

	return False, None

def is_prime_number(number):
	count = 0
	for i in range(1, number + 1):
		if number % i == 0:
			count += 1

	if count <= 2:
		return True
	return False

prime_numbers = []
num = 2
while num <= 1500:
	check = 0
	for count in range(1, num + 1):
		if num % count == 0:
			check += 1
		
	if check <= 2:
		prime_numbers.append(num)
	num += 1

for result in range(10000, 1000000):
	boolean, ind = sequence(result, prime_numbers)
	if is_prime_number(result) and boolean:
		print(result, ind)


# алгоритм рабочий только есть один момент, что прогрмма долго волняется