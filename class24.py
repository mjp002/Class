a = [1, 2, 3]
b = ['a', 'b', 'c']
list(zip(a, b))



list(zip(a, b))


tuple(zip(a, b))


a = (1, 2, 3)
b = ['a', 'b', 'c']
list(zip(a, b))


a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['딸기', '복숭아', '참외']
d = list(zip(a, b, c))
d


def plus(a, b):
    return a+b

plus(4, 9)

import numpy as np
def plus(*args):
    return np.sum(np.array(args))

print(plus(3, 6, 9))

print(plus(3, 1, 5, 6, 4, 7))


def plus_multiple(a, *b):
    return a*np.sum(np.array(b))

print(plus_multiple(3, 6, 9))

print(plus_multiple(3, 1, 5, 6, 4, 7))


def plus_multiple(a, *b):
    n = len(b)
    for i in range(n):
        print(b[i])
    return a*np.sum(np.array(b))


plus_multiple(3, 1, 5, 6, 7, 4)


def plus(*args):
    print(np.sum(np.array(args)))

plus(3, 6, 9)


def plus_with_5(a, b, c = 5):
    return a + b + c

print(plus_with_5(1, 2))


print(plus_with_5(1, 2, 10))



a = 100
def plus_a(n):
    return n+a

plus_a(3)


del a
def plus_a(n):
    a = 100
    return a + n

plus_a(3)


print(a)


import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x, y)

plt.show()


plt.plot(x,y, linewidth = 4)
plt.show()


plt.figure(figsize = (6,6))
plt.scatter(x,y, c = 'g', s = 100, label = 'dot graph')
plt.plot(x,y, c = 'g', alpha = 0.5, label = 'line graph')
plt.grid()
plt.legend(fontsize = 20, loc = 4)
plt.xticks(fontsize = 14, color = 'b')
plt.yticks(fontsize = 25, color = 'y')
plt.xlabel('Sun light', color = 'c', fontsize = 19)
plt.ylabel('Apple sweet', color = 'm', fontsize = 30)
plt.title('y = 2x', fontsize = 30)
plt.show()
