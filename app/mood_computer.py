# Компьютерный датчик настроения
# Демонстрирует использование elif
import random

print('Я ощущаю вашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.')
print('Итак, ваше настроение...')
mood = random.randint(1, 3)
if mood == 1:
    # радостное
    print( \
        '''
        ___________
       |          |
       | 0    0   |
       |   <      |
       |          |
       |          |
       | '...'   |
       ___________
         
        ''')

elif mood == 2:
    # так себе
    print( \
        '''
        ___________
       |          |
       | 0    0   |
       |   <      |
       |          |
       |          |
       | ------  |
       ___________
        ''')
elif mood == 3:
    # прескверное
    print( \
        '''
        ___________
       |          |
       | 0    0   |
       |   <      |
       |    ,     |
       |  .  .    |
       | ,    , |
       ___________
        ''')
else:
    print('Не бывает такого настроения! (Должно быть, вы совершенно не в себе.)')
print('...Но вы это только сегодня!')
input('\n\nPress the enter key to exit.')
# Else выполняется абсолютно во всех случаях, когда не истинно ни одно из созданных вами условий.