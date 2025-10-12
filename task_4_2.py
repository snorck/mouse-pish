'''Задача 2: Подсчёт частоты элементов
Условие: Дана строка, состоящая из символов. 
Необходимо подсчитать частоту каждого символа в строке и вывести её.

string = "abracadabra"
# Вывод: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}'''

string = "abracadabra"

my_list = list(string)
result = {}

for i in range(len(my_list)):
    if my_list[i] not in result:
        result[my_list[i]] = 1
    elif my_list[i] in result:
        result[my_list[i]] = result[my_list[i]] + 1

print(result)