def generate_triangle_numbers():
	triangles = []
	for number in range(100):
		triangles.append(int(number * (number + 1) / 2))

	return triangles

def summa_triangle_words(string):
	alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	summa = 0
	for element in string:
		summa += alpha.index(element) + 1

	return int(summa)


counter = 0
quantity = 0
while True:
	with open("words.txt", "r", encoding="utf-8") as file:
		for word in file.readlines():
			try:
				string = word.split(",")[counter].strip('"')
				if summa_triangle_words(string) in list(generate_triangle_numbers()): 
					quantity += 1
				counter += 1
			except IndexError:
				print(quantity)
				exit(0)