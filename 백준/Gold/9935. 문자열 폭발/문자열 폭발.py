# 9935번 문자열 폭발

# 스택?

import sys
from collections import deque

str = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

new_str = []
for i in range(len(str)):
  new_str.append(str[i])
  n = len(target)
  if len(new_str) >= n:
    str_idx = -1
    search = new_str[-n:-1]
    search.append(new_str[-1])
    if search == target:
      for _ in range(n):
        new_str.pop()

if new_str:
  for str in new_str:
    print(str, end='')
else:
  print('FRULA')

# test = deque(['m', 'i', 'r'])
# target = deque('mi')

# print(test[-3:-1])
# print(test[-3:-1] == target)