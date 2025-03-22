import sys
from collections import deque

K = int(sys.stdin.readline())

money_stack = deque()

for _ in range(K):
  n = int(sys.stdin.readline())

  if n == 0:
    money_stack.pop()
  else:
    money_stack.append(n)

print(sum(money_stack))