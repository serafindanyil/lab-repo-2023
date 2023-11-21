from math import *
_interval = [0, 0.5]
h = 0.05
d = 0.01
_sum = 0
result = 1
m = 20
x = 0

while _interval[0] <= _interval[1]:
    print("condition =", round(_interval[0], 2), "\t", _sum)
    #x += h
    _sum = 0
    _interval[0] += h
    n = 1
    result = 1

    while fabs(result) >= d:
        result *= (pow(-1, n) * (m - n + 1) * pow(x, n) / factorial(n))
        _sum += result
        n += 1
    x += h

else:
    print("the end of lab2.2")



