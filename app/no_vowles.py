# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for

message = input('Введите текст: ')
new_message = ''
VOWELS = 'aeiouаеёиоуыэюя'

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        #print('Создана новая строка:', new_message)
print('\nВот ваш текст с изьятыми гласными буквами', new_message)
input('\n\nНажмите Enter, чтобы выйти.')

# 118