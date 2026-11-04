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
# n = input()
# print(n[-2:])
# print(n[2:])
# n1 = input()
# if n1 not in n:
#     print("no")
# else:
#     print("yes")