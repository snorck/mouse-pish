'''Задание 3: Подсчет количества слов
Дана строка, содержащая предложение:

sentence = "Python is a powerful and easy-to-learn programming language."
Напишите программу, которая:

Разделит предложение на отдельные слова.
Подсчитает, сколько слов в предложении.'''

sentence = "Python is a powerful and easy-to-learn programming language."

sentence = sentence.replace('-', ' ')
words_list = sentence.split(' ')

print(len(words_list))