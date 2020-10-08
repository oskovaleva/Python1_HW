# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salaries.txt') as f:
    lines = f.readlines()
    surnames, salaries = [i.split()[0] for i in lines], [int(i.strip().split()[1]) for i in lines]
    for i in zip(surnames, salaries):
        if i[1] < 20000:
            print(i[0])
    print(f'Average salary: {sum(salaries)/len(salaries):.2f}')
