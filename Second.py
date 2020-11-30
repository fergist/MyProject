from random import randint

massive = []
for i in range(10):
    massive.append(abs(randint(-40, 30)))
k = int(input('Введите k\n'))
a = []
for i in massive:
    if i // 10 == i % 10:
        continue
    elif i < 10:
        continue
    elif i // 10 == 1 or i % 10 == 1:
        if i // 10 == 0:
            a.append(k * 10 + i)
        else:
            a.append(k * 100 + i)
        continue
    a.append(i)
print(*massive)
print(*a)
