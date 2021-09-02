class Stationary:
    title = 'Parent'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationary):
    title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pensil(Stationary):
    title = 'Pensil'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Handle(Stationary):
    title = 'Handle'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

a = Stationary()
b = Pen()
c = Pensil()
d = Handle()

a.draw(), b.draw(), c.draw(), d.draw()
