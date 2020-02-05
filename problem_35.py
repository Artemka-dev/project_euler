import random
from itertools import permutations

def is_Number(number):
	counter = 0
	for num in range(1, number + 1):
		if number % num == 0: counter += 1

	if counter <= 2: return True
	else: return False

def rotates(number):
	ratations = []
	for i in range(0, 3):
		ratations = number[i:1] + number[i+1:]

	return ratations


def is_Round(number):
	if number < 10: return is_Number(number)

	strNumber = str(number)
	rot = rotates(strNumber)
	for item in rot:
		if is_Number(int("".join(item))) == False:
			return False
	return True

counterRoundNumbers = 0
for num in range(2, 1000000):
	if is_Number(num) and is_Round(num):
		print(num, counterRoundNumbers)
		counterRoundNumbers += 1

print(counterRoundNumbers)

# Задача решена не правильно