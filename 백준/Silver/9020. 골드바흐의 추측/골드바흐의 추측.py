# import math

# def prime(num):
#     # 1은 소수가 아님
#   if num == 1:
#     return False
#   if num == 2:
#     return True
#   for i in range(2, int(math.sqrt(num))+1):
#     # 나누어 떨어지면 소수가 아님
#     if num % i == 0:
#       return False
#   return True

import sys

T = int(sys.stdin.readline())

# for _ in range(T):
#   x = int(sys.stdin.readline())
#   temp = 0

#   for i in range(2, x//2+1):
#     if not prime(i):
#       continue
#     elif prime(x-i) and temp < i:
#       temp = i
#   print(f'{min(temp, x-temp)} {max(temp, x-temp)}')

import math

# 에라토스테네스의 체
prime = [False for i in range(10001)]
prime[0] = True
prime[1] = True

for i in range(2, int(math.sqrt(10000))):
  if prime[i] == True:
    continue
  for j in range(i+i, 10000, i):
    # i의 배수인 j는 소수가 아니다
    prime[j] = True

# 풀이
for _ in range(T):
  x = int(sys.stdin.readline())
  temp = 0

  for i in range(2, x//2+1):
    if not prime[i] and not prime[x-i] and temp<i:
      temp = i
  print(f'{min(temp, x-temp)} {max(temp, x-temp)}')
