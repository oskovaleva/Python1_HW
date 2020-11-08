# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class NewException(Exception):
    pass


def division(numerator, denominator):
    try:
        if denominator == 0:
            raise NewException
        print(numerator / denominator)
    except NewException:
        print('Denominator cannot be 0!')


division(10, 5)
division(10, 0)
division(float(input('Input a numerator: ')), float(input('Input a denominator: ')))
