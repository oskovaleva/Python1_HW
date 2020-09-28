user_list = []
while True:
    user_list.append(input('Input an element: '))
    if 'no' in input('Do you want to input another element? ').lower():
        break
print(user_list)

new_list = user_list.copy()
for el in range(len(new_list) // 2):
    new_list[0 + el * 2], new_list[0 + el * 2 + 1] = new_list[0 + el * 2 + 1], new_list[0 + el * 2]
print(new_list)
