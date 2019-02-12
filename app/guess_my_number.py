# Отгадай число
# Компьютер выбирает случайное число в диапозоне от 1 до 1000
# Игрок пытается отгадать это число,и компьютер говорит,
# предположение больше/меньше, чем загаданное число
# или попало в точку

import random

print('\tДобпро пожаловать в игру "Отгадай число"!')
print('\nЯ загадал натуральное число из диапазона от 1 до 100.')
print('У вас всего 7 попыток.\n')

# начальные значения
the_number = random.randint(1, 100)
guess = int(input('Ваше предположение: '))
tries = 1

# цикл отгадывания
while guess != the_number:
    if guess > the_number:
        print('Меньше...')
    elif tries :
        print('')
    else:
        print('Больше...')
    guess = int(input('Ваше предположение: '))
    tries += 1

print('Вам удалось отгадать число! Это в самом деле', the_number)
print('Вы затратили на отгадывание всего лишь', tries, 'попыток!\n')

input('\n\nPress the enter key, to exit.')
