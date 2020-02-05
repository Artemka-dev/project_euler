def get_point(sorted_mass):
	alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	point = 0
	for element in sorted_mass:
		for letter in element:
			point += (alpha.index(letter) + 1) * (sorted_mass.index(element) + 1)

	return point


mass = []
file = "0"
counter = 0
while True:
	with open("names.txt", "r", encoding="utf-8") as file:
		for element in file.readlines():
			try:
				word = element.split(",")[counter].strip('"')
				mass.append(word)
				counter += 1
			except IndexError:
				sorted_mass = list(sorted(mass))
				print(get_point(sorted_mass))
				exit(0)

# print(get_point(['COLIN']))