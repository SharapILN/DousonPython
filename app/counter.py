# Считалка
# Демонстрирует использованиe функции range()
print('Посчитаем: ')
for i in range(10):
    print(i, end=' ')
print('\n\nПеречислим кратные пяти: ')
for i in range(0, 51, 5):
    print(i, end=' ')
print('\n\nПосчитаем в обратном порядке: ')
for i in range(10, -1, -1):
    print(i, end=' ')
input('\n\nНаэмите Enter. чтобы выйти.')
