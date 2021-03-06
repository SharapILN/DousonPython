# Манипуляции с цитатой
# Демонстрирует строковые методы - это своего рода "способность", которая есть у строки.
# цитата из Томаса Уотсона, который в 1943 г. был директором IBM
quote = '\'Думаю, на мировом рынке можно будет продать штук пять компьютеров.\''
print('Исходная цитата: ')
print(quote)
print('\nОна же в верхнем регистре: ')
print(quote.upper())
print('\nВ нижнем регистре:')
print(quote.lower())
print('\nКак заголовок:')
print(quote.title())
print('\nС ма-а-ленькой заменой: ')
print(quote.replace('штук пять', 'несколько миллионов'))
print('\nА вот опять исходная цитата: ')
print(quote)

# Методы схожи с функциями, основное отличе в том, что стандратная функция, например такая, как input()
# может быть вызвана независимо ни от чего, а строковый метод обязательно применяется к конкретной строке.
# В скобки после метода, можно как и функциям передавать аргументы, но некоторые из них априори могут принимать
# никаких аргументов.

# TODO: ЗАПОМНИ! Строковые методы создают новые значения. Их работа никак не сказывается на исходной строке.

print('\nSwapcase: регистры наоборот.')
print(quote.swapcase())
input('\nНажмите Enter, чтобы выйти.')
