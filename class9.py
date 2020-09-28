a = 10
c = 0
while a > 0:
    c += a
    a -= 1

print(c)



a = 0
while a < 20:
    a += 1
print(a)


a = [1, 2, 3, 4, 5]
print('가장 적은 수는 : {}'.format(min(a)))
print('가장 큰 수는 : {}'.format(max(a)))



import numpy as np

a = [1, 2, 3, 4, 5]
b = np.array(a)

print(b)
type(b)

print (b[0], b[-5])
print(b[1], b[-4])
print (b[2], b[-3])
print (b[3], b[-2])
print (b[4], b[-1])


print(b[1:3])

print (b[::2])

c = b + 5
print(b)

print(c)


c = b/4
c

c = b**2
c


d = np.sqrt(c)
print(b)

print(c)

print(d)




a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.multiply(a, b)


print(np.max(a))

print(np.min(b))


np.random.randint(9)



np.random.randint(100, 130, size = 2)

import numpy as np
def lotto():
    number = []
    for i in range(6):
        new_element = np.random.randint(1, 46)
        if new_element not in number:
            number.append(new_element)
    return number


print (lotto())





