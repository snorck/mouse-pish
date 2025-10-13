'''
Задача 5: Проверка на анаграмму
Условие: Даны две строки. Необходимо определить, являются ли они анаграммами (содержат одинаковые символы с одинаковой частотой).

string1 = "listen"
string2 = "silent"
# Вывод: True
'''
string1 = "listen"
string2 = "silent"

my_list1 = list(string1)
my_list2 = list(string2)
result1= {}
result2= {}

for i in range(len(my_list1)):
    if my_list1[i] not in result1:
        result1[my_list1[i]] = 1
    elif my_list1[i] in result1:
        result1[my_list1[i]] = result1[my_list1[i]] + 1

for i in range(len(my_list2)):
    if my_list2[i] not in result2:
        result2[my_list2[i]] = 1
    elif my_list2[i] in result2:
        result2[my_list2[i]] = result2[my_list2[i]] + 1

print(result1 == result2)