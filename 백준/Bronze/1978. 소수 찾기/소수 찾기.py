def prime(num):
    # 1은 소수가 아님
  if num == 1:
    return False
  for i in range(2, num):
    # 나누어 떨어지면 소수가 아님
    if num % i == 0:
      return False
  return True

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

cnt = 0
for num in num_list:
  if prime(num):
    cnt += 1

print(cnt)