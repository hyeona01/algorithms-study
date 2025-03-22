import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
  stack.append(int(sys.stdin.readline()))

max_height = 0
count = 0
for _ in range(N):
  temp = stack.pop()
  if temp > max_height:
    max_height = temp
    count += 1

print(count)