from math import *
_interval = [2, 5]
h = 0.2
_tabulation = []
i = 0
i2 = 0

while _interval[0] <= _interval[1] + h:
    _tabulation.append(round(_interval[0], 2))
    _interval[0] += h

for x in _tabulation:
    if x < 3:
        print('\f', "condition 1: ", "x =", log(fabs(log(x) + (1 / sin(x)))))
    elif 3 <= x < 4:
        print("condition 2: ", "x =", (cos(x) / tan(x)) * (x + log(x)))
    elif x >= 4:
        print('\f', "condition 3: ", "x =", 1 / (16.1 - (x ** 2)))

else:
    print("the end of lab2.1")