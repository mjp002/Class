#다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비숫한 국가와 그 차이를 출력하세요.
#데이터
nationWidth = {
    'Korea' : 220877,
    'Russia' : 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900 }


w = nationWidth['Korea']
nationWidth.pop('Korea')
l = list(nationWidth.items())           #쌍으로 리스트
gap = max(nationWidth.values())         #최대 벨류를 기준잡기
item = 0

for i in l:
    if gap > abs(i[1] - w):
        gap = abs(i[1] - w)
        item = i

print(item[0], item[1] - 220877)


################################################################

# 1 부터 1000까지의 숫자중에 '1'이 들아가는 숫자를 세라.
## For 를 안 쓰고

print(str(list(range(1, 1001))).count('1'))   #문자열로 바꿔서 리스트로 만든후 1이 들어간 숫자를 셈

### 함수 설정

def count(n):    #함수 선언
    countN = str(list(range(n + 1))).count('1')    #문자열로 바꿔서 리스트를 만들고 그 리스트에 1을 포함하는 숫자를 셈
    return countN    #값 돌려놓기

print(count(1000))


##For 를 쓰고

def count(n):
    s = str(list(range(n+1)))
    count = 0
    for i in s:
        if i == "1":
            count += 1
    return count

print(count(1000))

##########################################################

#================hi================ 찍어내기

#포맷문
a = "hi"

print('{0:=^50}'.format(a)+'=')

#포맷 X

s = "hi"
print(('='*((50-len(s))//2)+ s +('='*(50-(50-len(s))//2))))


#이름 리스트
students = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']

students = sorted(students)
for number, name in enumerate(students):
    print("번호: {}, 이름: {}".format(number+1, name))


#화물 옮기기
a = int(input())
def min_labor(n):
    a = n // 7
    b = (n - a*7)//3
    if n != a*7 + b*3:
        return -1
    print('7kg: {}, 3kg: {}'.format(a,b))
min_labor(a)
min_labor(24)


a = int(input(127))
min_labor(a)



#quiz





#quiz 3,6,9 박수를 치는데 3,6,9 만 포함한 수에서 박수
def sol(n):
    n = list(str(n))
    answer = 0
    count = 1
    d = {3:1, 6:2, 9:3}

    while n:
        answer += d[int(n.pop())]*count
        count*=3
    
    return answer

## 학생 답변
def threesixnine(n):
    a = {'3','6','9'}
    result = 0
    for i in range(1, int(n)+1):
        if a.issuperset(set(str(i))) == True:
            result += 1
    return result


threesixnine(36)


#quiz 아마존 면접 문제
#모범답안

a=['a1','a2','a3','a4','an','b1','b2','bn']
for i in range(len(a)):
    a.append(a[0][1]+a[0][0])
    a.pop(0)
a.sort()

for i in range(len(a)):
    a.append(a[0][1] + a[0][0])
    a.pop(0)



print(a)



#다른형태
a=['a1','a2','a3','a4','an','b1','b2','bn']
for i in range(1,len(a)):
    for j in range(len(a)-i):
        if ord(a[j][0])+ord(a[j][1])>ord(a[j+1][0])+ord(a[j+1][1]):
            #아스키 코드값의 합 비교 j값이 j+1 값보다 크면 교환
            temp=a[j]
            a[j],a[j+1]



#다른 형태
a=['a1','a2','a3','a4','an','b1','b2','bn']
b=[]
c=[]
for i in a:
    b.append(i[1]+i[0])
b.sort()
for i in b:
    c.append(i[1]+i[0])
print(c)

#
def solution(전체블록, 규칙):
    answer = []
    for 부분블록 in 전체블록:
        answer.append(블록순서체크(부분블록, 규칙))
    return answer



def 블록순서체크(부분블록, 규칙):
    임시변수 = 규칙.index(규칙[0])
    for 문자 in 부분블록:
        if 문자 in 규칙:
            if 임시변수 > 규칙.index(문자):
                return '불가능'
            임시변수 = 규칙.index(문자)
    return '가능'



전체블록 = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEGFG', 'AEBFDGCH']
규칙  = 'ABCD'

temp = 0


print(solution(전체블록, 규칙))


## 코드가 순서대로 규칙에 맞게 돌아가게 하기



#class 30 알고라즘
#가장 긴 공통 부분 문자열 Longest Common Subsequence

