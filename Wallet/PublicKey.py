import os
import math
import random
import time
import hashlib

#Additive Operation
def addOperation(a, b, p, q, m):
    if q= (math.inf, math.inf):
        return p

    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]

    if p = q:

        #Doubling
        #slope (s) = (3 * x1^ 2 + a) / (2 * y1) mod m
        #분모의 역원부터 계산한다(by Fermat's Little Theorem)
        # pow() 함수가 내부적으로 Square-and-Multiply 알고리즘을 수행한다.
        r = 2 * y1
        rInv = pow(r, m-2, m) #Fermat's Little Theorem
        s = (rInv * (3 * (x1 ** 2) + a)) % m
    else:
        r = x2 - x1
        rInv = pow(r, m-2, m) #Fermat's Little Theorem
        s = (rInv * (y2-y1)) % m
        x3 =


