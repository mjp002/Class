a = 17
a_prime = True
for i in range(2,a):
    if a % i == 0:
        a_prime = False

    if a_prime == True:
        print('{}는 소수이다.'.format(a))
    else:
        print('{}는 소수가 아니다.'.format(a))


def is_prime(a):
    b = range(2, a)
    c=0
    for i in b:
        if a % i == 0:
            c += 1
        if c > 0:
            print('{}는 소수가 아니다.'.format(a))
            

        if c < 0:
            print('{}는 소수이다.'.format(a))
            

        return a

is_prime(31)


def is_prime2(a):
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


a = range(1, 101)       #100까지니 101까지 지정
prime_numbers = []      #소수 list를 공집합으로 우선 만들고
for i in a:             #1부터 100까지 중
    c = is_prime2(i)    #i가 소수이면 c는 True, 아니면 Flase 생성
    if c == True:       #c가 True이면
        prime_numbers.append(i)     #b에다가 i를 추가하라
print(prime_numbers)



def is_prime2(a):
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


a = range(2, 1001)              #range 설정
prime_numbers = [1]             #소수 list를 1부터 시작하게 만들기
diff = 0                        #소수와 그다음 소수까지의 차이를 우선 0으로

for i in a:
    c = is_prime2(i)
    if c == True:
        prime_numbers.append(i)
        if prime_numbers[-1] - prime_numbers[-2] > diff:
            diff = prime_numbers[-1] - prime_numbers[-2]
            max_diff_primes = [prime_numbers[-2], prime_numbers[-1]]


print ('소수사이 구간의 최대값 : {}'.format(diff))
print ('최대구간의 소수쌍 : {}'.format(max_diff_primes))


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




def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr

test = [12,13,11,14,10]
print(selection_sort(test))



s