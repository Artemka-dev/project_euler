def getDividers(number):
	# mass = [int(num) for num in range(1, number + 1) if number % num == 0]
	mass = []
	for num in range(1, number + 1):
		if number % num == 0:
			mass.append(num)

	return mass[:-1]

def isNumberFriendWith(dividers, number):
	summa = 0
	for div in dividers:
		summa += div

	result = getDividers(summa)
	massive = sum(result)
	if number == massive and number != summa:
		# return "d(" + str(number) + ") => " + str(summa)
		return True
	else:
		return False

count = 0
for number in range(1, 10000):
	dividers = getDividers(number)
	bollean = isNumberFriendWith(dividers, number)
	if bollean:
		count += number

print(count)