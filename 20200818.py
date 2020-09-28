import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.figure(figsize = (6, 6))
plt.scatter(x,y, c = 'g', s=100, label = 'dot graph')
plt.plt(x, y, c = 'r', linewidth = 4, alpha = 0.5)
plt.grid()
plt.xlim([0, 6])
plt.ylim([0, 12])
plt.legend(fontsize = 20, loc = 4)
plt.title('y = 2x', fontsize = 30)
plt.xlabel('Sun light', color = 'c', fontsize = 19)
plt.ylabel('Apple sweet', color = 'm', fontsize = 30)



plt.show()





import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 1)
b = np.arange(-5, 5, 2)
plt.figure(figsize = (5, 7))
for i in b:
    plt.plot(x, x + i, label = 'y = x + {}'.format(i))
plt.grid()
plt.legend(fontsize = 13)

plt.show()




import matplotlib.pyplot as plt
import numpy as np


a = 1
x = np.arange(-10, 11, 1)
plt.figure(figsize = (5, 8))
plt.scatter(x, 1/x)
plt.axvline(x = 0, c = 'k')
plt.axhline(y = 0, c = 'k')
plt.grid()

plt.show()





import matplotlib.pyplot as plt
import numpy as np

a = 2
x = np.arange(-10, 10, 1)
t = np.arange(-5, 6, 2)
plt.figure(figsize = (5, 5))
for i in t:
    plt.plot(x, a*(x-i), label = 'shift {}'.format(i))
plt.grid()
plt.legend()


plt.show()






import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

x = np.arange(-5, 11)
y = 3*x + 2
y2 = 3*x + 2 + 5
plt.plot(x, y, label = 'original')
plt.plot(x, y2, label = 'y : 5')
plt.legend(fontsize = 14)
plt.grid()


plt.show()





import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction


x = np.arange(-10, 11)
y = abs(x)
plt.plot(x, y, label = 'abs value')
plt.legend(fontsize = 14)
plt.grid()


plt.show()





#알고리즘 숙제 (input, split, map, list, sorted 를 이용)
a = input().split()


a = [1,1,2,2,3,3]
for i in range(len(a)):
    a[i] = int(a[i])


a = list(map(int, a))       ##map 함수는 하나씩 가져와서 집어넣는다



print(sorted(list(map(int, input('숫자입력: ').split())))[-1])



