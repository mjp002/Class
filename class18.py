a = [2*x for x in [3,4,5,6,8,9]]
a


b = [x % 7 for x in range(10,20)]
b


a = [2*x for x in [3,5,6,8,9] if x % 2 == 0]
a


def is_prime2(a):
    b = (2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        d = False
    else:
        d = True
    return d

d = [-x for x in range (1, 101) if is_prime2(x)]
print(d)



from fractions import Fraction

def prime_factorization(a):
    b = range(2, a)
    primes = []
    for i in b:
        while a % i == 0:
            primes,append(i)
            a /= i
    if primes == []:
    
    return primes



def finite_OX(a, b):
    finite = Trueprimes = prime_factorization(Fraction(a, b).denominator)
    for i in primes:
        if i != 2 and i != 5:
            finite = False
    return finite


e = [Fraction(1,x) for x in range(1, 101) if finite_OX(1, x)]
print(e)



for i in range(2, 101):
    if (i % 4 == 1) and (i % 5 == 1) and (i % 6 == 1):
        print(i)



for i in range (1, 31):
    if (i % 2 ==0) or (i % 3 ==0):
        print(i)



a = [1,2,3,4,5]
b = np.array(a)
print(b)
type(b)


import numpy as np
c = np.array([1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,15])



print(c[:0])



c.reshape(5,5)



import numpy as np

a = np.array(range(3, 121, 3))
b = a.reshape(8, 5)
print(b)

c = b.reshape(4, 10)
print(c)





import numpy as np
