# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('num_eng.txt') as en, open('num_ru.txt', 'w') as ru:
    lines = en.readlines()
    for line in lines:
        new_line = line.strip().split()
        new_line[0] = my_dict.get(new_line[0])
        print(' '.join(new_line), file=ru)
