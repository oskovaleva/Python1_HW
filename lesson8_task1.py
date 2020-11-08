# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_str):
        self._date = date_str
        Date.validate(self._date)

    @classmethod
    def date_to_num(cls, date_str):
        tmp_list = list(map(int, date_str.split('-')))
        return tmp_list[0], tmp_list[1], tmp_list[2]

    @staticmethod
    def validate(date_str):
        try:
            day, month, year = Date.date_to_num(date_str)
            if len(str(year)) != 4:
                print('Incorrect year input, should be YYYY!')
            if month > 12 or month < 1:
                print('Incorrect month input, should be a number from 1 to 12!')
            if day < 1 or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30)\
                    or (month == 2 and year % 4 == 0 and day > 29) or (month == 2 and year % 4 != 0 and day > 28):
                print('Incorrect day input, this date does not exist!')
        except ValueError:
            print('Incorrect input format, should be DD-MM-YYYY!')


Date.validate('1-1-2020')
print(Date.date_to_num('1-1-2020'))
Date.validate('1-13-2020')
Date.validate('32-1-2020')
Date.validate('1-1-20020')
Date.validate('31-06-2020')
Date.validate('1-1-200')
Date.validate('30-2-2020')
Date.validate('29-02-2021')
Date.validate('1-0-2020')
Date.validate('0-1-2020')
Date.validate('01:01:2020')
