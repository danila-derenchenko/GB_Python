import math

print("Program 1")

day = int(input("Введите номер дня недели: "))

if day == 6 or day == 7:
    print("Это выходной")
else:
    print("Это не выходной")

print("Program 2")

flag = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z) == (not(x) and not(y) and not (z)):
                flag = 1
            else:
                flag = 0
if flag == 1:
    print("Выражение истинно")
else:
    print("Выражение ложно")

print("Program 3")

x = int(input("Введите x: "))
y = int(input("Введите y: "))

if x > 0 and y > 0:
    print("Это первая четверть")
elif x < 0 and y > 0:
    print("Это вторая четверть")
elif x < 0 and y < 0:
    print("Это третья четверть")
elif x > 0 and y < 0:
    print("Это четвёртая четверть")
else:
    print("x и y не должны быть равны нулю")

print("Program 4")

a = int(input("Введите номер четверти: "))

if a == 1:
    print("И x и y должны быть положительными")
elif a == 2:
    print("x отрицательное, y положительное")
elif a == 3:
    print("И x, и y отрицательные")
elif a == 4:
    print("x положительное, y отрицательное")
else:
    print("Введён неверный номер четверти")

print("Program 5")

x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

print("Расстояние между двумя введёнными точками: " + str(math.dist((x1, y1), (x2, y2))))