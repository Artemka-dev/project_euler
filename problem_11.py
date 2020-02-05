mass = []
with open("for_problem_11.txt", "r", encoding="utf-8") as file:
	for item in file.readlines():
		mass.append(item.strip())

current = 0
for number in mass:
	if mass.index(number) < 4:
		pass

# problem 11 не решена задача