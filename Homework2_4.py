'''
Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.

Пример 5 2 8 
[-5 -4 -3 -2 -1 0 1 2 3 4 5] -> (-4 * 2 = -8)
'''


a = int(input('Введите первое чиcло: '))
x1 = int(input('Введите местоположение первого множителя: '))
x2 = int(input('Введите местоположение второго множителя: '))

b = a * -1
numbrs = []
count = 0


while b <= a:
    numbrs.append(b)
    b = b + 1
print(numbrs)

for i in range ((len(numbrs)+1)):
    if i == x1:
        count = numbrs[(i-1)]
    if i == x2:
        count = count * numbrs[(i-1)]
print(count)
