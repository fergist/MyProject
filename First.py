from random import randint

massive = []
for i in range(15):
    massive.append(abs(randint(-20, 50)))
cooki = []
k = int(input('Введите k\n'))
for i in range(len(massive)):
    if massive[i] // 10 == 5 or massive[i] % 10 == 5:
        continue
    elif massive[i] % (i + 1) == 0:
        if massive[i] // 10 != 0:
            cooki.append(k * 100 + massive[i])
        else:
            cooki.append(k * 10 + massive[i])
        continue
    cooki.append(massive[i])
print(*massive)
print(*cooki)
