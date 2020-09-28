x = (5 + 3)/2
x

x = (-10)/10
x


from fractions import Fraction

def linear_eq(a, b, c):
    x = Fraction((c-b), a)
    return x


linear_eq(2, -3, 5)



def linear_eq(a, b, c):
    x = Fraction((c-b), a)
    if x.denominator == 1:
        x = int(Fraction(x))
    return x

linear_eq(2, -3, 5)


def linear_eq(a, b, c):
    if a == 0:
        if b == c:
            print('해가 무수히 많다.')
            return

    
    else:
        x = Fraction((c-b), a)
        if x.denominator == 1:
            x = int(Fraction(x))
        return


linear_eq(2, -3, 5)

linear_eq(0, 3, 4)

linear_eq(0, 3, 3)



from fractions import Fracrion
import numpy as np


class Linear_equation:
    def question(self):
        self.coefficient = np.random.randint(-10, 10)
        self.constant1 = np.random.randint(-20, 20)
        self.constant2 = np.random.randint(-20, 20)
        self.pm = np.random.randint(2)
        if self.pm == 0:
            print('{}x + {} = {}'.format(self.coefficient, self.constant1, self.constant2))
        elif self.pm == 1:
            print('{}x + {} = {}'.format(self.coefficient, self.constant1, self.constant2))

    def answer(self):
        if self.pm == 1:
            self.constant1 *= -1
        x = linear_eq(self.coefficient, self.constant1, self.constant2)
        return x



q1 = Linear_equation()
q1.question()

q1.answer()




##연습문제
for i in range(1, 100):
    if ((i+100)//i == 10) and ((i+100)%i == 1):
        print(2*i+100)



for x in range(1, 50):
    y = 50 - x
    if (y//x != 2) and (y%x == 3):
        print(x, y)



for i in range(1, 87):
    h = i - 2
    j = i + 2
    if ((h + i + j) == 87):
        print(h, i, j)


for x in range(1, 100):
    if x%2==1:
        if x+(x+2)+(x+4)==87:
            print(x+4)


for i in range(14, 100, 10):
    s=str(x)
    if int(s[1]+s[0])+9==x:
        print(x)





def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
        if c > 0:
            d = False
        else:
            d = True
        return d


is_prime(31)


a = range(1, 101)
prime_numbers = []      
for i in a:
    c = is_prime2(i)
    if c == True:
        prime_numbers.append(i)
print(prime_numbers)



def solution(n):
    answer = 0
    snumber = []
    #...1
    for i in range(n +1):
        number.append(i)
    #...1
    for i in rnage(2, n+1, 1):
        if i == -1:
            coninue 
            j = 0
            for i in range(i+i, n+1, i):
                number[j] = -1





##알고리즘 HW
#모범답안

S = [1, 3, 4, 8, 13, 17, 20]

shortest = S[1]-S[0]
index = 0

for g in range(1, len(S)):
    if S[g]-S[g-1] < shortest:
        shortest = S[g]-S[g-1]
        index = g


