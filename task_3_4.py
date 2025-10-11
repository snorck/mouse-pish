'''Поиск максимальной суммы подмассива фиксированной длины
Дан список целых чисел и длина подмассива k. 
Нужно найти подмассив длины k, сумма элементов которого будет максимальной.
# Вход:
array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3
# Выход:
[3, 4, -1]  # Сумма 6
'''
array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3
max_summ = 0
for i in range(k):
    max_summ = max_summ + array[i]
for i in range(len(array)-k+1):
    temp_summ = 0
    for j in range(i, i+k):
        temp_summ = temp_summ + array[j]
    if temp_summ > max_summ:
        max_summ = temp_summ
        result = array[i:i+k]
print(result)  
   
