import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
nums = deque(sys.stdin.readline().strip())

stack = []

cnt = 0
for num in nums:
  while stack and stack[-1] < num and cnt < K:
    cnt += 1
    stack.pop()
  stack.append(num)

# 987654 의 경우 k만큼 제거하지 못함
while cnt < K:
  stack.pop()
  cnt += 1

for num in stack:
  print(num, end='')