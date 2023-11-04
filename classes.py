class Segment1:
    """ Одномерный отрезок."""

    # инициализация объекта класса (конструктор объекта класса)
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        dist = self.length()
        self.dist = dist

    def __repr__(self):
        s = f'[{self.start}, {self.finish}]'
        return s

    # метод
    def length(self):
        """ Возвращает длину отрезка"""
        # d = b.length()
        return self.finish - self.start

    def shift(self, dx):
        """ Сдвигает ЭТОТ отрезок на dx"""
        # b.shift(2)
        self.start = self.start + dx
        self.finish += dx


a = Segment1(2, 10)  # 1) выделяется память, 2) расписать память данными (инициализация объекта)
b = Segment1(-6, 1)

d = a.length()  # Segment1.length(a)
print(f'Отрезок от {a.start} до {a.finish} длиной {d}')

d = b.length()
print(f'Отрезок от {b.start} до {b.finish} длиной {d}')  # -6 1
b.shift(2)
print(f'Отрезок от {b.start} до {b.finish} длиной {d}')  # -4 3

a = b  # переменная a ссылается на тот же объект, на который ссылалась переменная b

print(f'Отрезок от {a.start} до {a.finish} длиной {d}')
print(f'Отрезок от {b.start} до {b.finish} длиной {d}')
b.start = 666
print(f'Отрезок {a} длиной {d}, {id(a)}')  # [666, 3]
print(f'Отрезок {b} длиной {d}, {id(b)}')
