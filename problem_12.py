# n(n + 1) / 2 - triangle number

def getTriangleDividers():
	divs = []
	triangle = 0

	for number in range(1000, 20000):
		triangle = 0
		triangle = int(number * (number + 1) / 2)
		for num in range(1, triangle + 1):
			if triangle % num == 0:
				divs.append(num)
		print(triangle, len(divs))
		if len(divs) > 500:
			return "TRIANGLE: " + str(triangle)
		divs = []

print(getTriangleDividers())
