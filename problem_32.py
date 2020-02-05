def generate_pan_multiply():
	summa = []
	for i in range(1, 100):
		for x in range(1, 100):
			result = str(i * x) + str(i) + str(x)
			if int(result) not in summa:
				if is_pan_number(int(result)):
					print("I:", i, " X:", x, " Returned:", result + str(i) + str(x))
					summa.append(int(result))
			
	return sum(summa)

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

print(generate_pan_multiply())