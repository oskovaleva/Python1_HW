n = int(input('Input number n: '))
multiplier = 10
number = 0
result = 0
count = 0
max_count = 3

while count < max_count:
    number += n * (multiplier ** count)
    result += number
    count += 1

print(result)
