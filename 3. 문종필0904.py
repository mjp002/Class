# 어떠한 수 n 이 될 때까지 다음의 두 과정 중 하나를 반복적으로
# 선택하여 수행하려고 한다. 단, 두번째 연산은 n 이 k로 나누어 
# 떨어질때만 선택할 수 있다.
# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다
# 예를 들어 n이 17, k가 4라고 가정하자. 이때 1번의 과정을 한번
# 수행하면 n은 16이 된다. 이후에 2번의 과정을 두 번 수행히면 n은 
# 1이 된다. 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
# 이는 n을 1로 만드는 최소 횟수이다.
# n과k가 주어질때 n이 1이 될때까지 1번 혹은 2번의 과정을 수행해야
# 하는 최소 횟수를 구하는 프로그램을 작성하시오.




n, k = map(int, input().split())
result = 0

while True:
  if n % k != 0:
    n = n - 1
    result = result + 1
    if n == 1:
      break
  
  else:
    n = n / k
    result = result + 1
    if n == 1:
      break

print(result)




n, k = map(int, input().split())
result = 0
