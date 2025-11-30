import argparse

parser = argparse.ArgumentParser(description='Обработка аргументов командной строки')
parser.add_argument('-f','--filename', help='Имя файла для обработки')
parser.add_argument('-m', '--month', type=int, help='Статистика за конкретный месяц')
#parser.add_argument('-h', '--help', help='Вывод справки')

args = parser.parse_args()

print(f"Файл: {args.filename}")
print(f"Подробный вывод: {args.month}")
