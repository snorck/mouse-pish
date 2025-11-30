import csv
import argparse

# Многострочная строка с описанием программы
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

def main_program(filename, target_month=None):
    # Словарь для преобразования числового представления месяца в текстовое
    month_name_set= {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель',
                      '05': 'Май', '06': 'Июнь', '07': 'Июль', '08': 'Август', 
                      '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
    
    # Инициализация словарей для хранения статистики
    month_temp_set = {}        # Сумма температур по месяцам
    month_measure_cout_set = {} # Количество измерений по месяцам
    month_avg_set = {}         # Средняя температура по месяцам
    month_min_temp = {}        # Минимальная температура по месяцам
    month_max_temp = {}        # Максимальная температура по месяцам
    
    # Открытие CSV файла для чтения
    with open(filename, 'r') as file:
        # Создание объекта reader для чтения CSV
        reader = csv.reader(file)
        row_num = 0            # Счетчик строк
        error_count = 0        # Счетчик ошибок
        
        # Цикл по всем строкам файла
        for row in reader:
            row_num += 1       # Увеличение счетчика строк
            
            # Замена пробелов на нули в первой колонке
            row[0] = row[0].replace(' ', '0')
            
            # Проверка, что температура является числом
            try:
                int(row[0].split(';')[5])
            except ValueError:
                # Обработка ошибки преобразования в число
                print('Ошибка в строке', row_num, row[0])
                print('не используем при расчете')
                error_count += 1
                
            else:
                # Получение номера месяца из данных
                current_month = row[0].split(';')[1]
                # Получение значения температуры
                current_temp = int(row[0].split(';')[5])

                # Если указан конкретный месяц, пропускаем другие месяцы
                if target_month and current_month != target_month:
                    continue

                # Если месяц встречается впервые
                if current_month not in month_temp_set:
                    # Инициализация данных для нового месяца
                    month_temp_set[current_month] = current_temp
                    month_measure_cout_set[current_month] = 1
                    month_min_temp[current_month] = current_temp
                    month_max_temp[current_month] = current_temp
                else:
                    # Обновление статистики для существующего месяца
                    month_temp_set[current_month] += current_temp
                    month_measure_cout_set[current_month] += 1
                    
                    # Обновление минимальной температуры
                    if current_temp < month_min_temp[current_month]:
                        month_min_temp[current_month] = current_temp
                    
                    # Обновление максимальной температуры
                    if current_temp > month_max_temp[current_month]:
                        month_max_temp[current_month] = current_temp

    # Расчет средней температуры для каждого месяца
    for month in month_temp_set:
        month_avg_set[month] = round(month_temp_set[month] / month_measure_cout_set[month])     
        
    # Вывод промежуточных результатов для тестирования
    # print(month_avg_set)
    # print(month_min_temp)
    # print(month_max_temp)

    # Если указан конкретный месяц, выводим только его статистику
    if target_month:
        if target_month in month_name_set:
            print('Статистика за', month_name_set[target_month])
            print('Среднемесячная температура:', month_avg_set[target_month])
            print('Минимальная температура:', month_min_temp[target_month])
            print('Максимальная температура:', month_max_temp[target_month])
        else:
            print(f"Месяц {target_month} не найден в данных")
        return

    # Полная годовая статистика
    # Инициализация переменных для годовой статистики
    year_max_temp = month_max_temp['01']  # Начальное значение из января
    year_min_temp = month_min_temp['01']  # Начальное значение из января
    year_avg_temp = 0                     # Сумма средних температур за год
    
    # Вывод статистики по месяцам и расчет годовых показателей
    for month in month_name_set:
        # Пропускаем месяцы, которых нет в данных
        if month not in month_avg_set:
            continue
            
        # Вывод названия месяца и статистики
        print(month_name_set[month])
        print('Среднемесячная температура:', month_avg_set[month])
        print('Минимальная температура:', month_min_temp[month])
        print('Максимальная температура:', month_max_temp[month])
        print()
        
        # Накопление данных для годовой статистики
        year_avg_temp += month_avg_set[month]
        
        # Обновление годового минимума
        if month_min_temp[month] < year_min_temp:
            year_min_temp = month_min_temp[month]
        
        # Обновление годового максимума
        if month_max_temp[month] > year_max_temp:
            year_max_temp = month_max_temp[month]
    
    # Расчет средней годовой температуры
    year_avg_temp = round(year_avg_temp / len(month_temp_set))
    
    # Вывод годовой статистики
    print('Среднегодовая температура:', year_avg_temp)
    print('Минимальная температура за год:', year_min_temp)
    print('Максимальная температура за год:', year_max_temp)

# Обработка аргументов командной строки через argparse
# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(description='Обработка данных о температуре из CSV файла')
# Добавление аргумента для указания файла (обязательный)
parser.add_argument('-f', '--file', required=True, help='Входной файл CSV для обработки')
# Добавление аргумента для указания месяца (опциональный)
parser.add_argument('-m', '--month', help='Статистика за указанный месяц (01-12)')
    
# Парсинг аргументов командной строки
args = parser.parse_args()
    
# Форматируем номер месяца к двузначному формату если нужно
if args.month:
    if len(args.month) == 1:
        target_month = '0' + args.month
    else:
        target_month = args.month
else:
    target_month = None
    
# Вызов основной программы с переданными аргументами
main_program(args.file, target_month)