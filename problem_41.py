def is_prime_number(num):
	count = 0
	for i in range(1, num + 1):
		if num % i == 0:
			count += 1

	if count <= 2: return True
	else: return False

def is_pan_number(number):
	count = 0
	mass = [int(i) for i in str(number)]
	for i in range(min(mass), min(mass) + len(mass)):
		# от минимального до минимального + длина массива
		if i in mass:
			count += 1

	if count == len(mass):
		return True
	else:
		return False

# current = 0
# for item in range(100000, 500000):
# 	if is_prime_number(item) and is_pan_number(item):
# 		print(item)
# 		if item > current:
# 			current = item
# print(current)
print(is_prime_number(7652413), is_pan_number(7652413))