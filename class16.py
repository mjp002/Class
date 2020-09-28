import numpy as np


class Integer:
    def question(self):
        self.constant = np.random.randint(low = -10, high = 10, size = 2)
        self.pm = np.random.randint(5)
        self.exponent= np.random.randint(low = 2, high = 4)
        if self.pm == 0:
            print('{}와 {}의 덧셈을 구하라'.format(self.constant[0], self.constant[1]))
        elif self.pm == 1:
            print('{}와 {}의 뺄셈을 구하라'.format(self.constant[0], self.constant[1]))
        elif self.pm == 2:
            print('{}와 {}의 곱셈을 구하라'.format(self.constant[0], self.constant[1]))
        elif self.pm == 3:
            print('{}와 {}의 나눗셈을 구하라'.format(self.constant[0], self.constant[1]))
        else:
            print('{}^{} = ?'.format(self.constant[0], self.exponent))
    
    def answer(self):
        if self.pm == 0:
            return self.constant[0] + self.constant[1]
        elif self.pm == 1:
            return self.constant[0] - self.constant[1]
        elif self.pm == 2:
            return self.constant[0] * self.constant[1]
        elif self.pm == 3:
            return self.constant[0] / self.constant[1]
        else:
            return self.constant[0]**self.exponent




q1 = Integer()
q1.question()


q1.answer()
a = -7

def answer_check(self):
    if q1.answer == a:
        print("정답입니다.")
    else:
        print("오답입니다.")
    return


a = -5
np.abs(5)


print((-2) + 7)
print(7 + (-2))

print(((-2)+(-3)) + +4)
print((-2)+((-3)+ +4))



5 + (-3) * (-2)**2

(3+2*(5-7))*4-10


from fractions import Fraction
print(Fraction(5/2))
print(Fraction(2.5))
print(Fraction(5,2))


Fraction(7,9).numerator
Fraction(7,9).denominator


Fraction(2,4)



class Rational_number:
    def question(self):
        self.constant = np.random.randint(low = -10, high = 10, size = 4)
        self.pm = np.random.randint(4)
        if self.pm == 0:
            print('({}/{}) + ({}/{})'.format(self.constant[0], self.constant[1]))
        elif self.pm == 1:
            print('({}/{}) - ({}/{})'.format(self.constant[0], self.constant[1]))
        elif self.pm == 2:
            print('({}/{}) * ({}/{})'.format(self.constant[0], self.constant[1]))
        else:
            print('({}/{}) / ({}/{})'.format(self.constant[0], self.constant[1]))

    def answer(self):
        if self.pm == 0:
            return self.constant[0] + self.constant[1]
        elif self.pm == 1:
            return self.constant[0] - self.constant[1]
        elif self.pm == 2:
            return self.constant[0] * self.constant[1]
        else:
            return self.constant[0] / self.constant[1]



q1.Rational_number()
q1.question()
q1.answer()




def prime_factorization(a):
    b = range(2, a)
    primes = []
    for i in b:
        while a % i == 0:
            primes.append(i)
            a /= i
    if primes == []:
        primes.append(a)
    return primes

print(float(Fraction(1,4)))
a = Fraction(1,4)
prime_factorization(a.denominator)





##유한소수 판별기

