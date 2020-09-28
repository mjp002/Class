x = range(1, 9, 1)
y = range(1, 5, 1)
xy = []



for i in x:
    for j in y:
        if i + 2*j == 8:
            xy.append([i,j])
print(xy)
print(len(xy))




# x + y = 60
# x + 2y = 12



x = [2, 3, 5, 7]
a = []
for i in x:
    if 3 * i + 2 <= 11:
        a.append(True)
    else:
        a.append(False)

a



x = [2, 3, 5, 7]
a = [3*i + 2 <= 11 for i in x]
a



x = [2, 3, 5, 7]
a= [i for i in x if 3*i + 2 <=11]
a


x = [2, 3, 5, 7]
a = [i for i in x if 4*i -5 > 13]
a

a = [i for i in x if 2*i +1 < 15]
a

print([i for i in range(-10, 11) if 3*i -7 <= 3])


print(list(filter(lambda i : 3*i -7 <= 3, range)))


a = []
for i in range(-10, 11):
    if 3*i -7 <= 3:
        a.append(a)

print(a)







x = [2, 3, 5, 7]
a = []
for i in x:
    if 3*i + 2 <= 11:
        a.append(True)
    else:
        a.append(False)


a


x = [2, 3, 5, 7]
a = [i for i in x if 3*i + 2 <= 11]
a


x = [2, 3, 5, 7]
a = [i for i in x if 4*i -5 > 13]
a




x = [2, 3, 5, 7]
a = []
for i in x:
    if 3*i + 2 <= 11:
        a.append(True)
    else:
        a.append(False)


a


x = [2, 3, 5, 7]
a = [3*i + 2 <= 11 for i in x]
a

x = [2, 3, 5, 7]
a = [i for i in x if 3*i + 2 <= 11]
a

a = [i for i in x if 2*i + 1 < 15]
a



print([i for i in range(-10, 11) if 3*i -7 <= 3])



a = []
for i in range(-10, 11):
    if 3*i -7 <= 3:
        a.append(i)

print(a)


print([i for i in range(-10, 11) if 3*i -7 <= 3])


a = []
for i in range (-10, 11):
    if 3*i -7 <= 3:
        a.append(i)


print(a)




#알고리즘 HW
s = "aaabbbczzzza"
result = s[0]
count = 0

for i in s:
    if i == result[-1]:
        count += 1
    else:
        result += str(count) + i
        count = 1
result += str(count)
print(result)


