# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
# до целого числа.
#
# Сложение. Объединение двух клеток. Число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда
# метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки равняется 15, количество ячеек
# в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cells: int):
        self.cells = cells
        if self.cells <= 0 or not isinstance(self.cells, int):
            print("Wrong input! Amount of cells should be a positive integer number!")

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cells + other.cells)
        else:
            print("Second operand isn't a Cell class instance!")

    def __sub__(self, other):
        if not isinstance(other, Cell):
            print("Second operand isn't a Cell class instance!")
        elif self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print(f"This would result in negative or zero amount of cells.")

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.cells * other.cells)
        else:
            print("Second operand isn't a Cell class instance!")

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(round(self.cells / other.cells))
        else:
            print("Second operand isn't a Cell class instance!")

    def __str__(self):
        return f"{str(self.cells)}"

    def make_order(self, num):
        return ('*' * num + r"\n") *\
               (self.cells // num if self.cells % num != 0 else self.cells // num - 1) + '*' *\
               (self.cells % num if self.cells % num != 0 else num)


cell1 = Cell(15)
cell2 = Cell(12)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
print(cell2.make_order(5))
print(cell1.make_order(4))
print(cell2.make_order(4))
