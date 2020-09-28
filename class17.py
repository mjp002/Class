from fractions import Fraction

def prime_factorization(a):
    b = range(2,a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(a)
    return primes


def finite_OX(a,b):
    finite = True






import numpy as np
np.sqrt(3)
np.pi

np.pi * np.sqrt(3)

plus_5 = lambda x: x+5
plus_5(7)

plus_5(np.array([1,2,3,4,5]))

a = lambda x, y: x+y
a(2, 6)


even = lambda x : x % 2 == 0
print(even(np.array([range(1,11)])))






BMI = lambda weight, height: weight / (height)**2
print(BMI(68, 1.75))

def fat_or_not(weight, height):
    bmi = BMI(weight, height)
    print('당신의 BMI는 {}입니다'.format(bmi))
    if bmi > 35:
        print('고도 비만입니다.')
    elif 30 <= bmi < 35:
        print('중등도 비만입니다.')
    elif 25 <= bmi < 30:
        print('경도 비만입니다.')
    elif 23 <= bmi < 25:
        print('과체중입니다')
    elif 18.5 <= bmi < 23:
        print('정상입니다.')
    elif bmi < 18.5:
        print('저체중입니다.')

fat_or_not(74, 1.68)





list(filter(even, range(1, 11)))

list(filter(lambda x: x % 2 == 0, [3,1,4,2,9]))


list(filter(even, range(1, 11)))

list(filter(lambda x: x % 2 == 0, [3,1,4,2,9]))



a = [3,1,4,2,9]

def even(n):
    if x % 2 == 0:
        return True
    else:
        return False

even_numbers = []
for i in a:
    if even(i):
        even_numbers.append(i)

print(even_numbers)


