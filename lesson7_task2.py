# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def materials_expense(self):
        pass


class Coat(Clothes):
    def __init__(self, v: float):
        self._v = v

    @property
    def materials_expense(self):
        return self._v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h: float):
        self._h = h

    @property
    def materials_expense(self):
        return 2 * self._h + 0.3


class CompositeClothes(Clothes):
    def __init__(self, children: list):
        self.children = children

    @property
    def materials_expense(self):
        materials_expense = 0
        for i in self.children:
            materials_expense += i.materials_expense
        return materials_expense


coat = Coat(52)
print(coat.materials_expense)
suit = Suit(10)
print(suit.materials_expense)
total = CompositeClothes([coat, suit])
print(total.materials_expense)
