#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Figure
from deq import Deq

f = Void()
t = Deq()
count, i = 0, 0
Figure._count = 0
try:
    print('Triangle :')
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
    Figure.fixed_triangle = t
    print('Convex :')
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, g = {f.g()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
