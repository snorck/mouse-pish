'''Задача 1: Уникальные элементы
Условие: Дана строка, содержащая несколько слов. 
Найдите все уникальные слова в строке и выведите их в алфавитном порядке.

sentence = "apple banana apple orange banana kiwi"
# Вывод: ['apple', 'banana', 'kiwi', 'orange']'''

sentence = "apple banana apple orange banana kiwi"

words_sentence = sentence.split()

sentence_set = set(words_sentence)

result = sorted(list(sentence_set))

print(result)
