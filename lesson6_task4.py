# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print('машина повернула ' + direction)

    def show_speed(self):
        print(f'текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость автомобиля: {self.speed}')
        if self.speed > 60:
            print('вы превысили скорость')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость автомобиля: {self.speed}')
        if self.speed > 40:
            print('вы превысили скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(70, 'white', 'Nissan')
print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
town_car.go()
town_car.show_speed()
sport_car = SportCar(200, 'red', 'Porsche')
print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_police)
sport_car.show_speed()
sport_car.stop()
work_car = WorkCar(50, 'black', 'Kia')
print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
work_car.turn('налево')
work_car.show_speed()
police_car = PoliceCar(60, 'blue', 'Ford')
print(police_car.speed, police_car.color, police_car.name, police_car.is_police)
police_car.turn('направо')
police_car.show_speed()
