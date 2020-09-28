def prime_factorization(a):
    b = range(2, a)
    primes = []
    for i in b:
        while a % 1 ==0:
            primes.append(i)
            a /= 1
    if primes == []:
        primes.append(a)
    return primes






import numpy as np

def least_common_multiple(a, b):
    c = prime_factorization(a)
    d = prime_factorization(b)
    for i in c:
        if i in d:
            d.remove(i)
    e = c + d
    f = 1
    for i in e:
        f*=i
    return f






def list_to_number(a):
    number = ''
    for i in range(len(a)):
        number = number + str(a[i])
    number = int(number)
    return number


def digit_expand(a, n):
    digit_10 = []
    while a // n != 0:
        e = a % n
        digit_10.append(e)
        a //= n
    digit_10.append(a)
    digit_10.reverse()

    return digit_10


def Number_system_change(number, n, m):
    num_str = str(number)
    len_num = len(num_str)

number_10 = 0
for i, num in enumerate(num_str):
    num_int = int(num)
    if num_int >= n:
        print('{}는 {}보다 크거나 같으니 {}진법의 수가 아니다.'.format(num_int, n, m))
        break
    else:
        number_10 += num_int*n**(len_num-i-1)

number_m = digit_expand(number_10, m)
return number_m

a = Number_system_change(621, 7, 10)
b = Number_system_change(3213, 4, 10)
a = list_to_number(a)
b = list_to_number(b)
print(a)
print(b)
print('{}개의 수가 있다.'.format(a-b))



