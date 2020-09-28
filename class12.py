a = 17
b = range(2, a)
primes = []
for i in b:
    while a % i == 0:
        primes.append(i)
        a /= i


if primes == []:
    primes.append(a)

    primes






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




print (prime_factorization(128))

print (prime_factorization(497))







a = 24
b = range(1, 24)
factors = []
for i in b:
    if a % i == 0:
        factors.append(i)
factors.append(a)
print(factors)





def factorization(a):
    b = range(1, a)
    factors = []
    for i in b:
        if a % i == 0:
            factors.append(i)
factors.append(a)

print (factorization(36))






def intersection(a,b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    return c



def greatest_common_factor(a, b, show = False):
    c = factorization(a)
    d = factorization(b)
    if show:
        print (c)
        print (d)
    e = intersection(c,d)
    return max(e)

a = 36
b = 96

greatest_common_factor(a, b)



def least_common_multiple(a, b):
    c = prime_factorization(a)
    d = prime_factorization(b)
    for i in c:
        if i in d:
            d.remove(i)
    e = c + d
    f = 1
    for i in e:
        f *= i
    return f

print (least_common_multiple(36, 96))

print (least_common_multiple(4, 7))




a = 325
digit_10 = []
while a // 10 != 0:
    e = a % 10
    digit_10.append(e)
    a //= 10

digit_10.append(a)
print (digit_10)
digit_10.reverse()
print(digit_10)




def digit_expand(a, n):
    digit_10 = []
    while a // n != 0:
        e = a % n
        digit_10.append(e)
        a //= n
    
    digit_10.append(a)
    digit_10.reverse()


    return digit_10




############################################################################

#Class 12 복습하기

############################################################################



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



print(digit_expand(1589.54))



try:
    num = eval(input("입력하시오:"))
    if num - int(num):
        print("소수입니다.")
    else:
        print("정수입니다.")
except:
    print('math error')




def Number_system_change(number, n, m):
    num_str = str(number)
    len_num = len(num_str)

    number_10 = 0

    for i, num in enumerate(num_str):

        num_int = int(num)
        if num_int >= n:

            print('{}는 {}보다 크거나 같으니 {} 짐법의 수가 아니다.'.format(num_int, n, n))

            break
            
        else:
            number_10 += num_int*n**(len_num-i-1)

        
    number_m = digit_expand(number_10, m)
    return number_m


Number_system_change(325, 10, 7)

Number_system_change(5023, 7 ,9)





import numpy as np

class Natural_number:
    def question(self):
        self.select = np.random.randint(5)
        self.n1 = np.random.randint(100)
        self.n2 = np.random.randint(100)
        self.n3 = np.random.randint(low = 2, high = 10)
        self.n4 = np.random.randint(low = 2, high = 30)

        if self.select == 0:
            print('{}가 소수인지 판별하소, 소수가 아니면, 악수를 구해라.'.format(self.n1))

        elif self.select == 1:
            print('{}와 {}의 최대공약수를 구하여라,'.format(self.n1, self.n2))
        
        elif self.select == 2:
            print('{}와 {}의 초소골배수를 구하여라.'.format(self.n3, self.n4))
        
        elif self.select == 3:
            print('{}를 2진법으로 나타내어라.'.format(self.n1))

        elif self.select == 4:
            self.n4_2 = digit_expand(self.n4, 2)

            print('2진수[{}]를 10진법으로 나타내어라.'.format(', '.join(mamp(str,self.n4_2))))

        
def answer(self):
    if self.select == 0:
        if is_prime2(self.n1):
            print('{}는 소수이다.'.format(self.n1))
        else:
            print(factoriaztion(self.n1))
    
    elif self.select == 1:
        print(greatest_common_factor(self.n1, self.n2, show = False))
    
    elif self.select == 2:
        print(least_common_multiple(self.n3, self.n4))
    
    elif self.select == 3:
        print(digit_expand(self.n1, 2))

    elif self.select == 4:
        print(digit_expand(self.n4, 10))



    q1 = Natural_number()
    q1.question()


    q1 .answer()





    