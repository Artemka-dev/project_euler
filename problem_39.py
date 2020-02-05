def get_decision(number):
	mass = set()
	for a in range(1, number):
		for b in range(a, number):
			# for c in range(b, number):
			c = (a * a + b * b)**0.5
			if c == int(c) and a * a + b * b == c * c and a + b + c == number:
				c = int(c)
				mass.add(str(a) + " " + str(b) + " " + str(c))

	return number, mass, len(mass)

current_len = 0
for i in range(1, 1001):
	num, mass, len_ = get_decision(i)
	if len_ > current_len:
		current_len = len_
		print("P: " + str(num) + " Len: " + str(len_) + " Set:", mass)