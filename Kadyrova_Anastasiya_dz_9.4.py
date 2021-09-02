class Car:
     def __init__(self, speed, color, name, is_police=False):
          self.speed = speed
          self.color = color
          self.name = name
          self.is_police = is_police

     def go(self):
          print(f' {self.color} {self.name} поехала')

     def stop(self):
          print(f' {self.color} {self.name} остановилась')

     def turn(self):
          print(f' {self.color} {self.name} повернула')

     def show_speed(self):
          print(f'Скорость: {self.speed}')

     def check_police(self):
          print(f'Полицейская {self.is_police}')

class TownCar(Car):
     def __init__(self, speed, color, name):
          super().__init__(speed, color, name)

     def show_speed(self):
          print(f'Скорость: {self.speed}') if self.speed <= 60 else print('Превышена допустимая скорость')

     def check_police(self):
          print(self.is_police)

class SportCar(Car):
     def __init__(self, speed, color, name):
          super().__init__(speed, color, name)

class WorkCar(Car):
     def __init__(self, speed, color, name):
          super().__init__(speed, color, name)
     def show_speed(self):
          print(f'Скорость: {self.speed}') if self.speed <= 40 else print('Превышена допустимая скорость')

class PoliceCar(Car):
     def __init__(self, speed, color, name):
          super().__init__(speed, color, name, True)

     def check_police(self):
          print(f'Полицейская: {self.is_police}')

c = Car(40, 'white', 'Audi')
t = TownCar(70, 'black', 'BMW')
s = SportCar(40, 'red', 'Ferrari')
w = WorkCar(40, 'green', 'Lada')
p = PoliceCar(40, 'white', 'Skoda')

t.go(), t.turn(), t.stop()
t.show_speed(), t.check_police
print(f'Марка: {p.name}, цвет: {p.color}, скорость: {p.speed}, полицейская: {p.is_police} \n')