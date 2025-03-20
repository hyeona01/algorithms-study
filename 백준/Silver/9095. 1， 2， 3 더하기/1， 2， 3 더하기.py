# 1, 2, 3 더하기
# 재귀로 풀어보자

import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
count = 0
nums = [] # 총합이 n이 되어야 하는 1, 2, 3의 조합

def solution(n, total):
  global count

  if total <= 0:
    count += 1
    return
  
  for i in range(1, 4): # 1~3
    a = sum(nums)
    if a < n and a + i <= n:
      nums.append(i)
      solution(n, total-i)
      nums.pop()

for num in lst:  
  solution(num, num)
  print(count)
  count = 0