def is_palindrom(num):
	mass_1 = [str(i) for i in str(num)]
	mass_1.reverse()
	if mass_1 == list(str(num)):
		return True
	else:
		return False

def binary_system(number):
	mass = []
	while number != 0:
		num = number % 2
		number = number // 2
		mass.append(str(num))

	mass.reverse()
	return "".join(mass) # + " (2)"

summa = 0
for i in range(1, 1000000):
	if is_palindrom(binary_system(i)) and is_palindrom(i):
		print(i)
		summa += i
print(summa)