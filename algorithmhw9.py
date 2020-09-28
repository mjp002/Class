def func(numlist):
    even_count=0
    odd_count=0

    for x in numlist:
        if(x%2==0):
            even_count+=1
        else:
            odd_count+=1


    print("홀수 %s개, 짝수 %s개"%(odd_count, even_count))


func([3, 4, 5, 6, 7])
func([12, 16, 22, 24, 29])
func([41, 43, 45, 47, 49])



a = ['apple', 'melon', 'orange']
b = ['chicken', 'pig', 'cow']
b[1] = 'melon'


c = a + b
c



a = [1, 2, 3]
b = [3, 4, 5]

c = []
for i in a:
    if i in b:
        c.append(i)

print(c)



def union(a, b):
    c=[]
    for i in a:
        if i not in b:
            c.append(i)
    c = c + b
    c.sort()
    return c


    