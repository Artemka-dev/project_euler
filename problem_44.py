def generate_pentagons():
	pent = []
	for number in range(1, 1000):
		pent.append(int(number * (3 * number - 1) / 2))

	return pent

p = []
mass_1 = generate_pentagons()
mass_2 = generate_pentagons()
for i in mass_1:
	for x in mass_2:
		if i > x: 
			continue
		elif i + x in mass_1 and x - i in mass_1:
			print("I: " + str(i) + " X: " + str(x))
		print(i, x)