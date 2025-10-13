
import csv
import sys

help_data = '''
Приложение, считывает текстовый файл csv, 
состоящего из строк следующего формата:
YEAR;MONTH;DAY;HOUR;MINUTE;TEMPERATURE
dddd - год 4 цифры
mm - месяц 2 цифры
dd - день 2 цифры
hh - часы 2 цифры
mm - минуты 2 цифры
temperature - целое число от -99 до 99

Аргументы командной строки:
-m <номер месяца> - статистика за указанный месяц;
-h - эта информация;
-f <filename.csv> входной файл csv для обработки;
'''
def main_program():
    month_name_set= {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель',
                      '05': 'Май', '06': 'Июнь', '07': 'Июль', '08': 'Август', 
                      '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
    
    month_temp_set = {}
    month_measure_cout_set = {}
    month_avg_set = {}
    month_min_temp = {}
    month_max_temp = {}
    with open('temperature_small.csv', 'r') as file:
        reader = csv.reader(file)
        row_num = 0
        error_count = 0
        for row in reader:
            row_num += 1
            try:
                int(row[0].split(';')[5])
            except ValueError:
                print('Ошибка в строке', row_num, row[0])
                print('не используем при расчете')
                error_count += 1
                
            else:

                if row[0].split(';')[1] not in month_temp_set:
                    #добавляем новые месяцы в множества и задаем начальные значения
                    month_temp_set[row[0].split(';')[1]] = int(row[0].split(';')[5])
                    month_measure_cout_set[row[0].split(';')[1]] = 1
                    month_min_temp[row[0].split(';')[1]] = int(row[0].split(';')[5])
                    month_max_temp[row[0].split(';')[1]] = int(row[0].split(';')[5])
                else:
                    #считаем сумму температур по каждому месяцу и количество измерений и заносим в 2 множетсва
                    month_temp_set[row[0].split(';')[1]] += int(row[0].split(';')[5])
                    month_measure_cout_set[row[0].split(';')[1]] += 1
                    #считаем минимальнгую температуры в каждом месяце
                    if int(row[0].split(';')[5]) < month_min_temp[row[0].split(';')[1]]:
                        month_min_temp[row[0].split(';')[1]] = int(row[0].split(';')[5])
                    #считаем максимальную температуры в каждом месяце
                    if int(row[0].split(';')[5]) > month_max_temp[row[0].split(';')[1]]:
                        month_max_temp[row[0].split(';')[1]] = int(row[0].split(';')[5])

             
    
  #сичтаем среднее значение температуры по каждому месяцу заносим в set 
    for month in month_temp_set:
        month_avg_set[month] = round(month_temp_set[month] / month_measure_cout_set[month])     
        
    print(month_avg_set)
    print(month_min_temp)
    print(month_max_temp)

    year_max_temp = month_max_temp['01']
    year_min_temp = month_min_temp['01']
    year_avg_temp = 0
    for month in month_name_set:
        print(month_name_set[month])
        print('Среднемесячная температура:', month_avg_set[month])
        print('Минимальная температура:', month_min_temp[month])
        print('Максимальная температура:', month_max_temp[month])
        print()
        year_avg_temp += month_avg_set[month]
        if month_min_temp[month] < year_min_temp:
            year_min_temp = month_min_temp[month]
        if month_max_temp[month] > year_max_temp:
            year_max_temp = month_max_temp[month]
    year_avg_temp = round(year_avg_temp / 12)
    print('Среднегодовая температура:', year_avg_temp)
    print('Минимальная температура за год:', year_min_temp)
    print('Максимальная температураза год:', year_max_temp)

if sys.argv[1:] != []:
    match sys.argv[1]:
        case []:
            print(help_data)
        case 'h':
            print(help_data)
        case '-h':
            print(help_data)
        case '-f':
            main_program()
else: 
    main_program()




"""with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)"""