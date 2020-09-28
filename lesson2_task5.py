my_list = [7, 5, 3, 3, 2]
while True:
    user_number = int(input('Input a positive integer number: '))
    position = 0
    for el in my_list:
        if el >= user_number:
            position += 1
    my_list.insert(position, user_number)

    if 'no' in input('Do you want to input another number? ').lower():
        break
print(my_list)
