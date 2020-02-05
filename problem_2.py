# числа фибоначи

def generateFibonachi():
    mass = [1, 2, 3]
    for i in range(3, 100):
        count = mass[i - 1] + mass[i - 2]
        if count < 4000000:
            mass.append(count)
        else:
            break
        
    return mass

def even(mass):
    summa = 0
    for i in mass:
        if i % 2 == 0:
            summa += i
        else:
            pass

    return summa

mass = generateFibonachi()
res = even(mass)
print(res)