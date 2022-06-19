import random

c = random.randint(1, 10)
d = random.randint(1, 2)

print('Давай сыграем. Угадай число и цвет. У Вас 5 попыток.')
a = int(input('Введите число от 1 до 10: '))
b = int(input('Введите цвет, где 1-Красное, 2-Черное: '))
count = 0

while True:
    if a != c and b == d:
        print('Неугадали')
    elif a == c and b != d:
        print('Неугадали')
    elif a != c and b != d:
        print('Неугадали')
    else:
        print('Вы выйграли')
        break
    a = int(input('Введите число от 1 до 10: '))
    b = int(input('Введите цвет, где 1-Красное, 2-Черное: '))
    count += 1
    if count == 4:
        if d == 1:
            print('Вы истратили все попытки. Было:', c, 'Красное')
        else:
            print('Вы истратили все попытки. Было:', c, 'Черное')
        break