# Случайные буквы
# Демонстрирует индексацию строк
import random

word = 'Ильнур'  # 0, 1, 2, 3, 4, 5 | -6, -5, -4, -3, -2, -1
print('В перменной word хранится слово:', word)
high = len(word)  # длина слова
low = -len(word)  # длина ( - ) слова
for i in range(10):
    position = random.randrange(low, high)
    print('word[', position, ']\t', word[position])
input('\n\nPress the enter key, to exit')
