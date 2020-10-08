# Создать текстовый файл (не программно), сохранить в нем несколько строк.
# Выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt') as f:  # file 'text.txt' created in task 1
    lines = f.readlines()
    print(f'Number of lines: {len(lines)}')
    lines_len = [len(i.split()) for i in lines]
    for ind, el in enumerate(lines_len, 1):
        print(f'Number of words in line {ind}: {el}')
