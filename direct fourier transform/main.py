from math import cos, sin, pi
import matrix
from matrix import vec
from sympy import *

print("\n\n NOT MATRIX мейд бай питонист №2 )\n")


def estimate(n):
    a = []
    bufc = 0  #for cos
    bufs = 0  #for sin
    for k in range(8):
        temp = cos(k * n * pi / 4).simplify()
        temp2 = sin(k * n * pi / 4).simplify()
        print(" /Доп/ cos and sin :", vec[k], "*( ", temp, " - i*", temp2, " )")
        if temp != 0:
            temp *= vec[k]
            bufc += temp
        if temp2 != 0:
            temp2 *= vec[k]
            bufs += temp2
        a.append(str(temp) + "I*" + str(-temp2))
        if bufc != 0 and k != 0:
            bufc.simplify()
        if bufs != 0 and k != 0:
            bufs.simplify()
    if bufs == 0 and bufc == 0:
        print(0)
    else:
        print("########## N = ",n, "###############")
        print("1/8 *(I*(", -bufs, ") + ", bufc, ")")
        print("#################################")


for a in range(8):
    estimate(a)

