# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

duration_in_seconds = int(input('Input duration in seconds: '))
multiplier = 60

hours = duration_in_seconds // (multiplier ** 2)
minutes = (duration_in_seconds % (multiplier ** 2)) // multiplier
seconds = duration_in_seconds % multiplier

hh = str(hours)
if hours < 10:
    hh = '0' + hh
mm = str(minutes)
if minutes < 10:
    mm = '0' + mm
ss = str(seconds)
if seconds < 10:
    ss = '0' + ss

print(f'{hh}:{mm}:{ss}')
