goods_list = []
good_id = 0
parameters = ['название', 'цена', 'количество', 'eд']
while True:
    good_id += 1
    good_info = {}
    for el in parameters:
        user_input = input(f'{el.capitalize()}: ')
        if user_input.isdigit():
            user_input = int(user_input)
        good_info.update({el: user_input})
    goods_list.append((good_id, good_info))
    if 'нет' in input('Хотите добавить еще один товар? ').lower():
        break
print(goods_list)

dict_analytics = {}
for el in parameters:
    tmp_list = []
    for element in goods_list:
        tmp_list.append((list(element).pop()).get(el))
    dict_analytics.update({el: tmp_list})
print(dict_analytics)
