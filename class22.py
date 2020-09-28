import numpy as np
from fractions import Fraction


def simultaneous_eq(a, b):
    a = np.array(a)
    b = np.array(b)
    c = b*Fraction(a[0], b[0])
    d = a - c
    y = Fraction(d[2],d[1])
    x = Fraction(a[2]-a[1]*y, a[0])
    return x, y


a = [2, 3, 4]
b = [3, -4, -4]
x, y = simultaneous_eq(a, b)
print(x, y)


a = [5, 2, 14]
b = [2, 1, 4]
c = [[5, 2], [2, 1]]
d = [14, 4]
result = np.linalg.solve(c, d)
result


def cnvt(s):
    l = list(s)
    for k in range(1, len(l), 2):
        if l[k].isdigit():
            l[k] = '*'
    return ''.join(l)

print(cnvt("57uyft43yut89574389"))


