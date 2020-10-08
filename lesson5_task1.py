# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('text.txt', 'w') as f:
    while True:
        user_input = input('What do you want to add into the file? (To exit press "Enter") >>> ')
        if user_input == '':
            break
        print(user_input, file=f)
