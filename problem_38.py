def is_sorted(string):
	mass = [int(i) for i in string]
	if sum(mass) == 45 and len(set(string)) == 9:
		return True
	else:
		return False

def getPan_number(number):
	degr = 1
	string = ""
	while len(string) != 9:
		string += str(number * degr)
		if is_sorted(string) == True and len(string) == 9:
			return string
		elif len(string) > 9:
			return None
		degr += 1

	return None

current = 0
for number in range(1, 1000000):
	result = 1
	big_num = getPan_number(number)
	print(number, big_num)
	if big_num:
		result = int(big_num)
	else:
		continue

	if result > current:
		current = result

print(current)