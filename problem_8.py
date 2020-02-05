mass = []
current = 0
with open("for_problem_8.txt", "r", encoding="utf-8") as file:
	for item in file.readlines():
		mass.append(item.strip())

data = str("".join(mass))

for i in range(0, len(data) - 13):
	part = data[i:i + 13]
	product = 1
	for char in part:
		product *= int(char)

	if product > current:
		current = product

print(current)


