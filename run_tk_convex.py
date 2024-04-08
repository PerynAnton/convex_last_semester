#!/usr/bin/env -S python3 -B
from deq import Deq
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


def void_draw(self, tk):
    for n in range(TkDrawer.triangle.size()):
        tk.draw_line(TkDrawer.triangle.last(), TkDrawer.triangle.first())
        TkDrawer.triangle.push_last(TkDrawer.triangle.pop_first())
    pass


def point_draw(self, tk):
    for n in range(TkDrawer.triangle.size()):
        tk.draw_line(TkDrawer.triangle.last(), TkDrawer.triangle.first())
        TkDrawer.triangle.push_last(TkDrawer.triangle.pop_first())
    tk.draw_point(self.p)


def segment_draw(self, tk):
    for n in range(TkDrawer.triangle.size()):
        tk.draw_line(TkDrawer.triangle.last(), TkDrawer.triangle.first())
        TkDrawer.triangle.push_last(TkDrawer.triangle.pop_first())
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(TkDrawer.triangle.size()):
        tk.draw_line(TkDrawer.triangle.last(), TkDrawer.triangle.first())
        TkDrawer.triangle.push_last(TkDrawer.triangle.pop_first())
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

Figure._count = 0
tk = TkDrawer()
tk.clean()
print("triangle :")
a = R2Point()
b = R2Point()
c = R2Point()
t = Deq()
t.push_first(b)
if b.is_light(a, c):
    t.push_first(a)
    t.push_last(c)
else:
    t.push_last(a)
    t.push_first(c)
TkDrawer.triangle = t
Figure.fixed_triangle = t
print("\nТочки плоскости")
f = Void()
try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, g = {f.g()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
