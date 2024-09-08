# name = input('Введите Ваше имя: ')
# if name == 'Steve':#== - проверка равенства
#     print('Здравствуйте, Администратор!')# Обязательно Tab или 4 пробела
# if name == 'Степан':
#     print('Здравствуй, Хозяин!!!')
# else:
#     print('Привет, ', name)
number = int(input('Введите число: ')) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число не подходит')

# or - and Самое маловероятное условие помещаем наверх
