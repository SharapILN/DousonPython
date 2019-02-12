import random

# Задачи. Глава 3.
# Напишите программу- симулятор пирожка с «сюрпризом», - которая бы при запуске отображала один из
# пяти различных «Сюрпризов», выбранный случайным образом.
print('\t\tДобро пожаловать на раздачу бесплатных пирожков с сюрпризом.')
print('Не стоит переживать, вас ожидают вкусные сюрпризы, которые вас не разочаруют!')

pie_num = random.randint(1, 5)

if pie_num == 1:
    print('Вам достался пирожок с вишней! Приятного аппетита!')
elif pie_num == 2:
    print('Вам достался пирожок со сгущенкой! Приятного аппетита!')
elif pie_num == 3:
    print('Вам достался пирожок с ванилью! Приятного аппетита!')
elif pie_num == 4:
    print('Вам достался пирожок с творогом! Приятного аппетита!')
elif pie_num == 5:
    print('Вам достался пирожок с клубникой! Приятного аппетита!')
else:
    print('Попробуйте снова!')
print('\nСледующая программа. "Орел или решка?"\n\n\n ')

# Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и сообщала, сколько раз выпал
# орел, а сколько - решка.
throw = 0
eagle = 0
tails = 0
while throw < 100:
    coin = random.randint(0, 1)
    if coin == 0:
        eagle += 1
    elif coin == 1:
        tails += 1
    throw += 1
print('Орел:', eagle)
print('Решка:', tails)

print('\nСледующая программа. "Отгадай число"\n\n\n ')

# Измените программу «Отгадай число» таким образом, чтобы у игрока было ограниченное количество попыток.
# Если игрок не укладывается в заданное число (и проигрывает), то программа должна выводить сколь
# возможно суровый текст.

