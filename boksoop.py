#문자열 연산하기

#문자열 더해서 연결하기(Concentation)
head = "Python"
tail = " is fun!"
head + tail

#문자열 곱하기
a = "Python"
a*2


#문자열 곱하기 응영
print("="*50)
print("My Program")
print("="*50)


#문자열 길이 구하기
a = "Life is too short"
len(a)

#문자 인덱싱
a = "Life is too short, You need Python"
a[0:3]

#슬라이싱 기법으로 단어 수정하기
a = "Pithon"
a[:1] + "y" + a[2:]

#두개 이상의 값 넣기
number = 10
day = "three"
"I ate {} apples. so I was sick for {} days".format(number, day)

#문자 개수 세기(Count)
a = "hobby"
a.count('b')


a = []
for i in range(1, 10001):
    i.count('8')
    print(i.count('8'))



def quick_sort(arr):

    n = len(arr)

    if n <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [7, 3, 1, 6, 5, 2, 4]
print(quick_sort(arr))



def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}는 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}는 소수이다.'.format(a))
        d = True
    return d

is_prime(31)



def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}는 소수가 아니다.'.format(a))
    else:
        print('{}는 소수인다.'.format(a))
    return d


#위키에 나오는 코드 에라토스테네스
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return[i for i in range(2, n) if sieve[i] == True]



prime_list(1)


prime_list(10)

prime_list(20)




def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


gcd(221, 143)





def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}은 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}은 소수이다.'.format(a))
        d = True
    return d



is_prime(55)



def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a    


gcd(112, 44)



def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}는 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}는 소수이가.'.format(a))
        d = True
    return d


def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

gcd(221, 143)




#딕셔너리
#{} 을 이용한다.
#딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a

#딕셔너리 요소 삭제
del a[1]
a
a['b']

#딕셔너리 key 리스트
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
for k in a.keys():
    print(k)

#소수
def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}는 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}는 소수이다.'.format(a))
        d = True

#유클리드
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

#연습문제
#1
a = {'국어':80, '영어':75, '수학':55}
a.keys()
a.values()
a = 80
b = 75
c = 55
(a+b+c)/3

a = "881120-1068234"
a[1:]


a = [0, 1, 2, 3, 4]
for idx, val in enumerate(fruit):
    print(idx, val)



import numpy as np
class Natural_number:
    def question(self):
        self.select = np.random.randint(5)
        self.n1 = np.random.randint(100)
        self.n2 = np.random.randint(100)
        self.n3 = np.random.randint(low = 2, high = 10)
        self.n4 = np.random.randint(low = 2, high = 30)
        if self.select == 0:
            print('{}가 소수인지 판별하고, 소수가 아니면, 약수를 구해라.'.format(self.n1))
        elif self.select == 1:
            print('{} 와 {} 의 최대공약수를 구하여라.'.format(self.n1, self.n2))
        elif self.select == 2:
            print('{} 와 {}의 최소공배수를 구하여라.'.format(self.n3, self.n4))
        elif self.select == 3:
            print('{}를 2진법으로 나타내어리.'.format(self.n1))
        elif self.select == 4:
            self.n4_2 = digit_expand(self.n4, 2)
            print


#일차방정식 생성기
import numpy as np
from fractions import Fracrion
class Linear_equation:
    def question(self):
        self.coefficient = np.random.randint(-10, 20)
        self.constant1 = np.random.randint(-20, 20)
        self.constant2 = np.random.randint(-20, 20)
        self.pm = np.random.randint(2)
        if self.pm == 0:
            print('{}x + {} = {}'.format(self.coefficinet, self.constant1, slrf.constant2))
        elif self.pm == 1:
            print('{}x - {} = {}'.format(self.coefficient, self.constant1, self.constant2))

            def answer(self):
                if self.pm == 1:
                    self.constant1 *= -1
                x = linear_eq(self.coefficient, self.constant1, self.constant2)
                return x




q1 = Linear_equation()
q1.question()



for i in range(1, 100):
    if ((i+100)//i == 10) and ((i+100)%i == 1):
        print(2*i+100)


for i in range(1, 50):
    j = 50 - i
    if (j//i != 2) and (j%i == 3):
        print(i,j)



for i in range(1, 100):
    if i%2==1:
        if i + (i + 2) + (i + 4)==87:
            print(i +4)


for x in range(1, 50):
    if (x-2) + x + (x+2) == 30:
        print(x-2)



for i in range(1, 100):
    if i + j == 60:
        if i + 12 == 2*j:
            print(i)


import numpy as np

a = []

x = np.arrange(1, 31)
discount = 6000 * 30 * 0.7
print('30명이 할인 받은 금액{}'.format(discount))

for i in x:
    if i*6000 <= discount:
        a.append(i)

print(a)
print(max(a))



#어떤 정수의 두배에서 3을 빼면 11보다 작고 이 정수의 세배에서
#6을 빼면 9보다 크다. 이때 정수를 구하시오

2*x-3 < 11
3*x-6 > 9



import numpy as np
x = np.arange(-10, 11)
b = lambda a: 3*a -7 <= 3
b(x)


a = []
for i in x:
    if 3*i -7 <= 3:
        a.append(i)
print(a)


def czip(a,b):
    if len(a) != len(b):
        print('길이가 달라요')
    else:
        n = len(a)
        c = []
        for i in range(n):
            c.append((a[i],b[i]))
        return c

a = [1, 2, 3]
b = ['a', 'b', 'c']




def is_multiple(a, b):
    while a >= b:
        a = a-b
        if a==b:
            return True

print(is_multiple(365,5))




#소수
def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a % i == 0:
            c += 1
    if c > 0:
        print('{}는 소수가 아니다.'.format(a))
        d = False
    else:
        print('{}는 소수이다.'.format(a))
        d = True

#유클리드
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a




#줄임말 출력하게 하기
user_input = input().split(' ')
#print(user_input)

result = ''

for s in user_input:
    result += s[0]

print(result)


##2
user = input('입력은 한글 혹은 영어로 입력됩니다.').split(' ')
for i in user:
    print(i[0], end='')

#코딩 경진대회 문제
a = input().split(',')
b = input().split(',')

c = []
count = 0

for i, j in zip(a, b):
    if count % 2 == 0:
        c.append([i, j])
    else:
        c.append([j, i])
    count += 1

print(c)


##zip을 안쓴 케이스
a = ['1', '2', '3', '4']
b = ['a', 'b', 'c', 'd']

result = []
for i in range(len(a)):
    if i % 2 == 0:
        result.append([a[i],b[i]])
    else:
        result.append([b[i],a[i]])



#민규 악수
def solution(n):            #n = 59
    people = 0              #전체 참가자 수
    total = 0               
    while(True):
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)         #민규 악수 수
    return [times, people]



##ver2
def solution(n):
    for x in range(n):
        for y in range(x):
            if x*(x-1)/2==n-y:
                return '민규의 악수 횟수 {}회, 행사 참가자 {}명'.format(y, x+1)


print(solution(59))





##
result = [x*y for x in range(2, 10) 
                for y in range(1, 10)]
print(result)



# 괄호 문자열이란 괄호 기호인 '(',')','[',']','{','}' 와 같은 것을 말한다. 그 중 괄호의 모양이 바르게 구성 된 문자열을 바른 문자열, 그렇지 않은 문자열을 바르지 않은 문자열이라 부르도록 하자.
# (())와 같은 문자열은 바른 문자열이지만 ()()) 와 같은 문자열은 바르지 않은 문자열이다. (해당 문제에서는 소돨호만 판별하지만, 실력이 되시는 분들은 중괄호와 대괄호까지 판별해보세요.)
# 입력으로 주어진 괄호 문자열이 바른 문자열인지 바르지 않은 문자열인지 "YES" 와 "NO"로 구분된 문자열을 출력해보자.

def math(a):
    if a.count('(') != a.count(')'):
        return False
    j = []
    for i in a:
        if i == '(':
            j.append('(')
        if i == ')':
            if len(j) == 0:
                return False
            j.pop()
    return True

n = input()
if math(n) == True:
    print("YES")
else:
    print("NO")




math('())')
math('(())')



##ver 2
def math(e):
    if '(' and ')' not in e:
        return False
    if list(e).count('(') == list(e).count(')'):
        print('YES')
        return True
    else:
        print('NO')
        return False



abs(3)
abs(-3)
abs(1.2)
all([1,2,3,0])
all([])
any([1,2,3,4])
any([1,2,3,0])
chr(50)
dir([1,2,3])
divmod(7,3)
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))



def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))



a = input()
a


b = input("Enter:")
b



divmod(2,2)

divmod(5,3)
eval('divmod(5,3)')


print('{0:_^60}'.format('jello'))



def comf(n):
    if len(n) <= 3:
        return n

    else:
        return comf(n[:len(n)-3]) + ',' +n[len(n)-3:]
    
comf('10000000000')




##20190923


string = 'aacddddddddd'
a=string.count('a')
b=string.count('b')
c=string.count('c')
d=string.count('d')
print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(d)+str(b)+str(a+1)))







bri = set(['brazil', 'russia', 'india'])
'india' in bri

'usa' in bri

bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
bri & bric





students = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']

students = sorted(students)
for number, name in enumerate(students):
    print("번호: {}, 이름: {}".format(number+1, name))


'{0:+^60}'.format('hi')
'{0:60}'.format('hello')
'{0:>60}'.format('hi')
'{0:0.5f}'.format(3.4851568416878)
'I have seen {0} horses galloping down the hill with my {1} eyes'.format(71,2)
'',''.join('abcd')



