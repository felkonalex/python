class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышение скорости! ваша скорость - {self.speed}'
        else:
            return f'Скорость {self.name} допустима'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость выше допустимой! Ваша скорость - {self.speed}'
        else:
            return f'Скорость {self.name} допустима'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('влево'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())