# Вариант 1

# Задание 1
S = input("Введите первую строку ")
S_0 = input("Введите вторую строку ")
d = ''
l_0 = len(S_0)
for i in range(len(S)):
    d += S[i]
    l_d = len(d)
    if S_0 not in S:
        print("Исходная строка", S)
        break
    elif d[-l_0:] == S_0:
        d = d[:-l_0] + S[l_d:]
        print("Исходная строка", S)
        print("Изменённая строка", d)
        break

# Задание 2
s = list(input("Введите предложение ").split())
if 1 < len(s) < 31:
    for j in range(len(s)):
        if len(list(s[j])) < 2 or len(list(s[j])) > 10:
            print("Ошибка, текст не соответстувует условию")
            break
        else :
            if s[j] != s[-1]:
                print(s[j])
else:
    print("Ошибка, текст не соответствует условию")

# Задание 3
import random

n = int(input("Введите количество элементов в списке "))
v = []
for j in range(n):
    v.append(random.randint(-10**3, 10**3))

print("Исходны список", v)
c = 0
summ = 0
mx = -10**9
pr = 1
mx_k = 0

for m in range(len(v)):
    if abs(v[m]) > mx:
        mx = abs(v[m])

for k in range(len(v)):
    if v[k] % 2 == 0:
        c += 1
        summ += v[k]
    if abs(v[k]) == mx:
        mx_k = k

for p in range(mx_k+1, len(v)):
        pr = pr * v[p]

print("Сумма элементов кратных 2:", summ)
print("Количество элементов кратных 2:", c)
print("Произведение элементов:", pr)
