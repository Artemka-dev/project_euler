def summaSquare():
	mass_1 = []
	for number in range(1, 101):
		mass_1.append(number ** 2)

	return sum(mass_1)

def squareSumma():
	num = 0
	for number in range(1, 101):
		num += number

	return num ** 2

summaS = summaSquare()
sSumma = squareSumma()

print(sSumma - summaS)