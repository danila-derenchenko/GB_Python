import math

print("Program 1")

d = float(input("Input d: "))

print(round(math.pi, len(str(d).split('.')[1])))

print("Program 2")

n = int(input("Input n: "))

def Factor(n):
    Ans = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.add(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.add(n)
    return Ans

print(Factor(144))

print("Program 3")

a = [2, 5, 7, 3, 2, 9, 3, 6, 45, 74, 72, 325, 45]

result = set()

for i in a:
    result.add(i)

print(result)

print("Program 4")

def coeffc(exp):
    coeffc = []
    for i in range(len(exp)):
        for j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if exp[i] == j and exp[i - 1] != "*":
                coeffc.append(exp[i])
    return coeffc

def constructor(exp):
    return str(exp[0]) + "x**2" + " + " + str(exp[1]) + "*x" + " + " + str(exp[2])

coeff1 = []
coeff2 = []

with open("file1.txt") as f:
    coeff1 = f.readline()

with open("file2.txt") as f:
    coeff2 = f.readline()

coeff1 = coeffc(coeff1)
coeff2 = coeffc(coeff2)
summcoeff = []
for i in range(len(coeff1)):
    summcoeff.append(int(coeff1[i]) + int(coeff2[i]))

print(constructor(summcoeff))