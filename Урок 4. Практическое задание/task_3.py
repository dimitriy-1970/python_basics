"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генераторное выражение.
"""
a = int(input('Введите первое число диапазона: '))

b = int(input('Введите последние число диапазона: '))

c = int(input('Введите число к которому ищем кратность: '))
print('Числа кратные в заданном диапазоне заданному числу', end='  ')
for i in range(a, b + 1):

    if i % c == 0:
        print(i, end='  ')

