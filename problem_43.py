def is_pan_number(number):
	count = 0
	for num in range(0, 10):
		if str(num) in number:
			count += 1

	return count == 10

ind = 0
mass = [2, 3, 5, 7, 11, 13, 17] # простые числа
summa = 0 
for number in range(1000000000, 9999999999):
	st = str(number)
	if is_pan_number(st) and len(set(st)) == len(list(st)):
		if int(st[1:4]) % mass[ind] == 0 and int(st[2:5]) % mass[ind + 1] == 0 and int(st[3:6]) % mass[ind + 2] == 0 and int(st[4:7]) % mass[ind + 3] == 0 and int(st[5:8]) % mass[ind + 4] == 0 and int(st[6:9]) % mass[ind + 5] == 0 and int(st[7:10]) % mass[ind + 6] == 0:
			summa += int(number)
			print(summa)
print("Summa:", summa)