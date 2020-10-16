# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        if isinstance(self.matrix, list) and isinstance(self.matrix[0], list):
            self.rows_num = len(matrix)
            self.columns_num = len(matrix[0])
            self._dimension_check()
        else:
            self._exit()

    def _exit(self):
        print('Wrong input!')
        exit()

    def _dimension_check(self):
        for row in self.matrix:
            if not (isinstance(row, list) and len(row) == self.columns_num):
                return self._exit()

    def __str__(self):
        return '\n'.join([f"{'   '.join(map(str, row))}" for row in self.matrix])

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows_num == other.rows_num and self.columns_num == other.columns_num:
            return Matrix([
                [self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns_num)]
                for i in range(self.rows_num)
            ])
        else:
            print("Both operands must be Matrix class instances with the same dimensions!")


matrix1 = Matrix([[31, 22, 37], [43, 51, 86]])
print('matrix1')
print(matrix1)
matrix2 = Matrix([[3, 5, 8], [2, 7, 1]])
print('matrix2')
print(matrix2)
matrix_sum = matrix1 + matrix2
print('matrix_sum')
print(matrix_sum)
