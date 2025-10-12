'''Задание 2: Извлечение email-адресов
Дана строка, содержащая текст с email-адресами:

text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"
Напишите программу, которая:

Извлечет все email-адреса из строки.
Сохранит их в список и выведет результат.'''

text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"

only_mails = text.split(': ')[1]

list = only_mails.split(', ')

print(list)