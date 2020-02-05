res = []
count = 10
while True:
    mass = []
    for i in str(count):
        k = 1
        for d in range(2, int(i) + 1):
            k *= d
        mass.append(int(k))
    if sum(mass) == count:
        res.append(count)
        print(res)
        count += 1
    else:
        if count == 100000: break
        else:
            count += 1
            continue
print(sum(res))