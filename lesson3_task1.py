# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

num1 = input('Input a numerator: ')
num2 = input('Input a denominator: ')


def division(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ValueError:
        result = 'One or both of your arguments is not a number! :('
    except ZeroDivisionError:
        result = 'You tried to make a division by zero! :('
    return result


print(division(num1, num2))
