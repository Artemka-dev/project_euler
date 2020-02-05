mass = []
with open("for_problem_13.txt", "r", encoding="utf-8") as file:
	for i in file.readlines():
		mass.append(i.strip())

mass = [int(i) for i in mass]
summaMass = str(sum(mass))
print(summaMass[0:10])