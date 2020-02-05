# число-палиндром

mass = []
for i in range(100, 1000):
	for x in range(100, i):
		res = list(str(i * x))
		if list(res) == list(reversed(res)):
			mass.append(int(i * x))
print(max(mass))