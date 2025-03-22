import sys
from collections import deque

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

stack = deque()
result = []

for i in range(N):
  while stack and stack[-1][1] < lst[i]:
    stack.pop()
  
  if stack:
    result.append(stack[-1][0])
  
  else:
    result.append(0)
  
  stack.append([i+1, lst[i]])

# print(result)
for item in result:
  print(item, end=' ')