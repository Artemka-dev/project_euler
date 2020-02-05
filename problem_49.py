from fuzzywuzzy import fuzz

def is_prime_number(num):
	count = 0
	for i in range(1, num + 1):
		if num % i == 0:
			count += 1

	if count <= 2:
		return True
	else:
		return False

def search_progretion():
	mass = []
	for number in range(1000, 10000):
		num_1 = number
		num_2 = number + 3330
		num_3 = number + 6660

		if is_prime_number(num_1) and is_prime_number(num_2) and is_prime_number(num_3):
			result_number = str(num_1) + str(num_2) + str(num_3)
			if fuzz.ratio(str(num_1), str(num_2)) == 75 and fuzz.ratio(str(num_2), str(num_3)) == 75:
				mass.append(int(result_number))
			
	return mass

print(search_progretion())