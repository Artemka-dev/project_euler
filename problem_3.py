def is_Number(number):
	counter = 0
	for num in range(1, number + 1):
		if number % num == 0: counter += 1

	if counter <= 2: return True
	else: return False

def func(number):
	simpleDivs = []
	for i in range(1, number + 1):
		result = 0
		if is_Number(i) == True and number % i == 0:
			simpleDivs.append(i)

	return simpleDivs + " " + max(simpleDivs)



print(func(600851475143))
