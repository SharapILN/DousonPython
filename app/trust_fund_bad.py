# Рантье (версия с ошибкой)
# Демонстрирует логическую ошибку

print(
    '''
                Рантье
Программа подсчитывает ваши ежемесячные расходы. Эту статистику нужно знать,чтобы
у вас не закончились деньги и вам не пришлось искать работу.
Введите сумму расходов по всем статьям, перечисляемым выше. Вы богаты - так не ме-
лочитесь, пишите суммы в долларах, без центов.    
    '''
)

car = int(input('Техничекое обслуживание машины \'Marcedes-Benz\': '))
rent = int(input('Съем роскошной квартиры на Манхэттене: '))
jet = int(input('Аренда самолета: '))
gifts = int(input('Подарки: '))
food = int(input('Обеды и ужины в ресторанах: '))
staff = int(input('Жалованье прислуги (дворецкий, повар, водитель, секретарь): '))
guru = int(input('Плата личному психоаналитику: '))
games = int(input('Компьютерные игры: '))
total = car + rent + jet + gifts + food + staff + guru + games
print('\nОбшая сумма: ', total)
input('\n\nНажмите Enter, чтобы выйти.')

# TODO: Важно понимать что функция input(), возвращает значения строкового типа.

# Необходимо преобразовать строковые значения в числовые.
