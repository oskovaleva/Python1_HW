# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w+') as f:
    f.write(input('Input a bunch of numbers divided by space bar >>> '))
    f.seek(0)
    print(sum([i for i in map(int, f.read().strip().split())]))
