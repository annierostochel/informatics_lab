#Вариант 1

import math

#Задание 1
z = float(input("Введите сторону пятиугольника "))
if z > 0:
    h = z * math.tan(math.radians(76)) / 2 #высота одного треуголника
    S_t = 0.5 * z * h #площадь одного треугольника
    S = S_t * 5
    print(S)
else:
    print("Ошибка, введите другое число")

#Задание 2
x = float(input("Введите x "))
y = 0
a = 0.365
if x < -2.5:
    y = a * math.sin(2*x + 1) ** 2
elif x >= 4:
    y = math.exp(x)
else:
    y = x * math.sin(x * a)
print(y)