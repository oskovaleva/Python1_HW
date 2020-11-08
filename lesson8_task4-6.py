# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру, например словарь. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod
import time


class OwnError(Exception):
    pass


class Warehouse:
    def __init__(self, max_count: int):
        self.max_count = max_count
        self.appliances_count = 0
        self.appliances_list = []

    def __str__(self):
        return str(self.__dict__)

    def store(self, appliances: list):
        try:
            if self.appliances_count + len(appliances) > self.max_count:
                raise OwnError
            self.appliances_list.extend(appliances)
            self.appliances_count += len(appliances)
        except OwnError:
            print('На складе недостаточно места!')

    def transfer(self, appliances: list, department: 'Warehouse'):
        try:
            for appliance in appliances:
                if appliance not in self.appliances_list:
                    raise OwnError
            for appliance in appliances:
                self.appliances_list.remove(appliance)
                self.appliances_count -= 1
            department.store(appliances)
        except OwnError:
            print('На складе нет такой оргтехники!')


class OfficeAppliances(ABC):
    def __init__(self, brand, model):
        self.type = self.__class__.__name__
        self.brand = brand
        self.model = model

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    @abstractmethod
    def get_info(self, *args):
        pass

    @abstractmethod
    def print_info(self, *args):
        pass


# перевод из электронного формата в бумажный
class Printer(OfficeAppliances):
    def get_info(self, file_name):
        with open(file_name, encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
        return lines

    def print_info(self, file_name):
        for line in self.get_info(file_name):
            print(line)


# перевод из бумажного формата в электронный
class Scanner(OfficeAppliances):
    def get_info(self, info):
        return [i for i in info]

    def print_info(self, info, file_name=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())):
        with open(file_name, 'w') as f:
            f.writelines(self.get_info(info))


# перевод из бумажного формата в бумажный
class Xerox(OfficeAppliances):
    def get_info(self, info):
        return [i for i in info]

    def print_info(self, info):
        for i in self.get_info(info):
            print(i)


# работа над проектом «Склад оргтехники» завершена, команды ниже добавлены для проверки работоспособности программы
printer1 = Printer('xerox', '101')
printer2 = Printer('xerox', '102')
warehouse1 = Warehouse(10)
warehouse1.store([printer1, printer2])
print(warehouse1)
warehouse2 = Warehouse(1)
warehouse2.store([printer1, printer2])

accounting_dep = Warehouse(2)
warehouse1.transfer([printer1], accounting_dep)
print(warehouse1)
print(accounting_dep)
warehouse1.transfer([1], accounting_dep)
