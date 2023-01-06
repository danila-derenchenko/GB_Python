import math
import sympy
from sympy import *

'''print("Program 1")

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

print(result)'''

print("Program 4")

a = "4*x**2+1*x+4"
res = ""

for i in range(len(a)):
    for j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if a[i] == j and a[i - 1] != "*":
            print(a[i])
