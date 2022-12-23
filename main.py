import math

print("Program 1")

a = [2, 3, 6, 7, 5]
sum = 0

for i in a:
    if a.index(i) % 2 != 0:
        sum += i
print(sum)

print("Program 2")

a = [2, 3, 5, 6]

first = 0
end = len(a) - 1

result = []

for i in range((len(a) // 2)):
    result.append(a[first] * a[end])
    first += 1
    end -= 1

print(result)

print("Program 3")

a = [1.1, 1.2, 3.1, 5, 10.01]

b = [round(math.modf(x)[0], 4) for x in a if round(math.modf(x)[0], 4) != 0.0]

print(max(b) - min(b))

print("Program 4")

a = bin(int(input("Input number: ")))
a = a[2:]

print(int(a))