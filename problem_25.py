def generateFibonachi():
    mass = [1, 1]
    length = 2
    while True:
        count = mass[length - 1] + mass[length - 2]
        mass.append(count)
        length += 1
        if len(str(count)) == 1000:
            return length
            break
        else:
            continue
    return mass

res = generateFibonachi()
print(res)