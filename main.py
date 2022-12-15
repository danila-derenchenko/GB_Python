print("Program 1")

number = input("Input number: ")
lenght = len(number)
number = int(number)
result = 0

for i in range(1, lenght + 1):
    result += number % 10
    number //= 10

print(result)

print("Program 2")

n = int(input("Input n: "))

pred = 1
result = []

for i in range(1, n + 1):
    pred *= i
    result.append(pred)
for i in result:
    print(i)

print("Program 3")

n = int(input("Input n: "))

result = [2]

number = 2

for i in range(n):
    number = (1 + (1 / number)) ** number
    result.append(number)

print(sum(result))

print("Program 4")

with open("test.txt") as f:
    positionsText = f.readlines()
    positions = [int(x) for x in positionsText]
    n = int(input("Input n: "))
    prom = []
    for i in range(-n, n + 1):
        prom.append(i)
    result = prom[positions[0]]
    positions.remove(positions[0])
    for i in positions:
        result *= prom[i]
    print(result)