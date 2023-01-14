from random import randint

N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
print("1 - по возрастанию, 2 - по убыванию")
B = int(input())

if B == 1:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

if B == 2:
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] < a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]

print(a)