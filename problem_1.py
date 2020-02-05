# числа кратные 3 или 5

mass = [int(i) for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]
print(sum(mass))