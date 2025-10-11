'''Разворот блоков в списке
Дан список чисел и размер блока. 
Нужно развернуть элементы в каждом блоке по отдельности. 
Если последний блок меньше по размеру, его нужно оставить без изменений.
# Вход:
array = [1, 2, 3, 4, 5, 6, 7]
block_size = 3

# Выход:
[3, 2, 1, 6, 5, 4, 7]'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
block_size = 3

start_num = 0
end_num = block_size - 1

for i in range(len(array) // block_size):
    if start_num == 0:
        array = array[:start_num] + array[end_num::-1] + array[end_num+1:]     
    else: 
        array = array[:start_num] + array[end_num:start_num-1:-1] + array[end_num+1:]
   
    start_num = start_num + block_size
    end_num = end_num + block_size

print(array)

