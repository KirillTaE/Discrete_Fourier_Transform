import math
from math import pi
from math import cos, sin
import sympy
from sympy import simplify
from sympy import *


def eul(n, k):
    if k != 0:
        print("\n")
    print("k = ", j, "; уГОЛ = pi*", k*n, "/4")
    x = cos(2*pi*k*n/8).simplify()
    y = sin(2*pi*k*n/8)
    print(x, " - i*", y)


for i in range(8):
    print('\n######### n = {} ###########'.format(i))
    for j in range(8):
        eul(i, j)