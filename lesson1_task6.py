result_current = int(input('Input current result in kilometers: '))
result_target = int(input('Input target result in kilometers: '))
day = 1
multiplier = 1.1

while result_current < result_target:
    day += 1
    result_current = result_current * multiplier
print(f'Your target will be achieved on day {day}')
