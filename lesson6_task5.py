# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title='ручка'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


class Pencil(Stationery):
    def __init__(self, title='карандаш'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


class Handle(Stationery):
    def __init__(self, title='маркер'):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


stationery = Stationery('some stationery')
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
