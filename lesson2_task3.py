# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = int(input('Input month as a number from 1 to 12: '))

seasons_list = ['winter', 'spring', 'summer', 'fall']
season = seasons_list[0] if user_month == 12 else seasons_list[user_month // 3]
print(f'The season is {season}')

seasons_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
                8: 'summer', 9: 'fall', 10: 'fall', 11: 'fall', 12: 'winter'}
print(f'The season is {seasons_dict.get(user_month)}')
