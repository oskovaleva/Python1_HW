user_number = int(input('Input a positive integer number: '))
multiplier = 10
max_digit = 0

while user_number > 0:
    if user_number % multiplier > max_digit:
        max_digit = user_number % multiplier
    user_number = user_number // multiplier

print(f'The maximum digit in this number is {max_digit}')
