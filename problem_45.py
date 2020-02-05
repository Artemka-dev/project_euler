# T = number * (number + 1) / 2
# T = number * (3 * number - 1) / 2
# T = number * (2 * number - 1)

triangles = []
pentagons = []
sixtagons = []
for number in range(1, 200000):
	triangles.append(int(number * (number + 1) / 2))
	pentagons.append(int(number * (3 * number - 1) / 2))
	sixtagons.append(int(number * (2 * number - 1)))

result = list(set(triangles) & set(pentagons) & set(sixtagons))
print(result)