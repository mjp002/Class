n = int(input("num?: "))
a=0;b=1
print('0', end='')
while b<=n:
    print(', %d' %b, end = '')
    a,b = b,a+b





oct(35)



pow(2, 4)

pow(3, 5)


list(range(5))

list(range(10))

list(range(5, 10))




list(range(1, 10, 2))

list(range(0, -10, -1))


round(4.6)

round(4.2)

round(5.678, 2)


sorted([3, 1, 2])
sort([1,2,5,3])


sorted(["zero"])


sorted("zero")

str(3)

str('hi')

str('hi'.upper())


tuple('abc')

tuple([1,2,3])


type("abc")

type(open("test", 'w'))


list(zip([1,2,3], [4,5,6]))

list(zip([1,2,3], [4,5,6], [7,8,9]))




import time

for i in range(10):
    print(i)
    time.sleep(1)



for i in range(10):
    print(i)




import random


def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))


import random

data = [1, 2, 3, 4, 5]
random.shuffle(data)
data



import webbrowser

webbrowser.open("http://google.com")


webbrowser.open("http://naver.com")


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val



class UpgradeCalculator(Calculator)
    def minus(self, val):
        self.value -= val



cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add (self, val):
        self.value += val
        if self.value > 100:
            self.value * 100


all([1, 2, abs(-3)-3])

chr(ord('a')) == 'a'


a = [-8, 2, 7, 5, -3, 5, 0, 1]

max(a) + min(a)


round(17/3, 4)

round(17/3)

int(17/3)

