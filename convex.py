from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def g(self):
        return 0.0

    # проверка с треугольником
    def _in(p):
        flag1 = True
        flag2 = False
        for n in range(Figure.fixed_triangle.size()):
            if p.is_light(Figure.fixed_triangle.last(),
                          Figure.fixed_triangle.first()):
                flag2 = True
                if (Figure.in_1(p, Figure.fixed_triangle.last(),
                                Figure.fixed_triangle.first())):
                    flag1 = False
            Figure.fixed_triangle.push_last(Figure.fixed_triangle.pop_first())
        return int(flag1 and flag2)

    # лежит ли в нутри единичной
    def in_1(p, a, b):
        x1_1 = p.x - a.x
        y1_1 = p.y - a.y
        x2_1 = b.x - a.x
        y2_1 = b.y - a.y
        x1_2 = p.x - b.x
        y1_2 = p.y - b.y
        x2_2 = a.x - b.x
        y2_2 = a.y - b.y
        mult1 = x1_1 * x2_1 + y1_1 * y2_1
        mult2 = x1_2 * x2_2 + y1_2 * y2_2
        if (mult1 <= 0) or (mult2 <= 0):
            distance = min(p.dist(a), p.dist(b))
        else:
            distance = abs(R2Point.area(p, a, b))/a.dist(b)
        return (distance <= 1)


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)

    def g(self):
        return Figure._in(self.p)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif r.is_inside(self.p, self.q):
            return self
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return Segment(self.p, r)

    def g(self):
        return Figure._in(self.p) + Figure._in(self.q)


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)

        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._count = Figure._in(a) + Figure._in(b) + Figure._in(c)

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def g(self):
        return self._count

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                self._count -= Figure._in(p)
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                self._count -= Figure._in(p)
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)
            self._count += Figure._in(t)

        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
