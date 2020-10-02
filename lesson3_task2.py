# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name='not defined', surname='not defined', birthday_year='not defined', city='not defined',
              email='not defined', phone_number='not defined'):
    print(f'name: {name}, surname: {surname}, birthday year: {birthday_year}, city: {city}, email: {email}, phone '
          f'number: {phone_number}')


user_data(surname='Ivanov', name='Ivan', city='Moscow')
