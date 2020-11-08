# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re} {'+' if self.im > 0 else '-'} {abs(self.im)}i"

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re + other.re, self.im + other.im)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re + other, self.im)
        else:
            print("Second operand must be a number (int, float or complex)!")

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            return ComplexNum(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNum(self.re * other, self.im * other)
        else:
            print("Second operand must be a number (int, float or complex)!")


complex_num1 = ComplexNum(1, 2)
complex_num2 = ComplexNum(3, -4)
print(complex_num1 + complex_num2, str(complex_num1 + complex_num2) == '4 - 2i')
print(complex_num1 * complex_num2, str(complex_num1 * complex_num2) == '11 + 2i')
