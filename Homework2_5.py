# Задание 5. Реализуйте алгоритм перемешивания списка.

a = int(input('Введите последнее число, в списке от 0 до '))
numbrs = []
for i in range (a + 1):
    numbrs.append(i)
print(numbrs)

temp = 0
for i in range(len(numbrs)):
    temp = numbrs[i]
    numbrs[i] = numbrs[a-i]
    numbrs[a-i] = temp
    a = a - 1

print(numbrs)

# сам не знаю как у меня это получилось, но что то получилось =)