print(13 % 7 + 26 % 7)





currency_rate = 0.15*1110

print('1위안은 {}원이다.'.format(currency_rate))




import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 11)
y = 2.0**x
plt.plot(x, y)

plt.grid()
plt.show()




import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11)
y = np.sqrt(x)
plt.plot(x, y)

plt.grid()
plt.show()




import numpy as np
import matplotlib.pyplot as plt


def ReLu(*inputs):
    result = np.sum(inputs)
    if result < 0:
        result = 0
    return result

print (ReLu(3,4,5,6,7))
print (ReLu(-9,3,5,4,-6))





import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def factorization(a):
    b = range(2,a)
    factors = []
    for i in b:
        while a % i == 0:
            factors.append(i)
    factors.appens(a)
    return factors


x = np.arange(1, 101)
y = []
for i in x:
    factors = factorization(i)
    len_factors = len(factors)
    y.append(len_factors)
plt.plot(x,y)
plt.grid()
plt.show()






import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(-10, 11)
y = 3*x +5
z = -2*y -10
plt.plot(x,z)
plt.grid()
plt.show()





import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

##with for
x = np.arange(1, 11)
pairs = [(i, i**2) for i in x]
print(pairs)

##withour for
y = x**2
pairs2 = list(zip(x,y))
print(pairs2)






import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

x = np.arange(0, 20)
a = np.random.randint(low = -5, high = 5, size = len(x))
y = x + a


plt.plot(x,y)
plt.show()






import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

price = 8000000000
saving = 4000000-1000000-1000000

n = price/saving
year = n // 12
month = n % 12
print('총 {}년 {}개월이 걸린다.'.format(year, month))

price = 800000000
saving = np.arange(0, 11000000, 1000000)
n = price / saving


plt.plot(saving, n)
plt.grid()
plt.show()







import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

years = np.arange(0, 61, 1)

bully = (years-20)*1000
salaryman = (years-27)*3000
doctor = (years-36)*15000


bully[:2] = 0
salarymans[:27] = 0
doctor[:36] = 0

plt.plot(years, bully, label = "BULLY")
plt.plot(years, salaryman, label = "SALARYMAN")
plt.plot(years, doctor, label = "DOCTOR")
plt.grid()
plt.legend(fontsize = 14)
plt.show()






from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.nounds)



