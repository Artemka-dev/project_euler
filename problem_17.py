from words import *


def algoritmToWords(from_, until):
	string = ""
	for number in range(from_, until + 1):
		# string = ""
		if number <= 10: string += until_ten[str(number)]
		elif number <= 20 and number > 10: string += until_twenty[str(number)]
		elif number > 20 and number <= 100:
			if int(str(number)[1]) == 0: 
				string += until_hundred[str(number)]
			else:
				decades = str(number)[0] # берем десятки
				string += until_hundred[str(decades) + "0"] + until_ten[str(number)[1]]
		elif number > 100 and number < 1000:
			decades = str(number)[0] # десятки
			hunds = str(number)[1] # сотни
			ones = str(number)[2] # единицы
			if int(hunds) == 0 and int(ones) == 0: 
				string += until_ten[str(decades)] + "hundred"
			elif int(hunds) == 0: 
				string += until_ten[str(decades)] + "hundredand" + until_ten[str(ones)]
			elif int(ones) == 0: 
				string += until_ten[str(decades)] + "hundredand" + until_hundred[str(hunds) + str(ones)]
			else:
				if 10 < int(str(hunds) + str(ones)) < 20:
					string += until_ten[str(decades)] + "hundredand" + until_twenty[str(hunds) + str(ones)]
				else:
					string += until_ten[str(decades)] + "hundredand" + until_hundred[str(hunds) + "0"] + until_ten[str(ones)]
		else:
			string += "onethousand"
		# print(string)

	return "".join(string.strip())

wordsFromAlg = algoritmToWords(1, 1000)
print(len(wordsFromAlg))