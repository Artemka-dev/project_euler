def getFactorial(num):
    k = 1
    for i in range(2, num + 1):
        k *= i
    return k

def summa(res_num):
    mass = [int(i) for i in res_num]

    print(sum(mass))

number = 100
res_num = getFactorial(number)
summa(str(res_num))