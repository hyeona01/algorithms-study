# 9935번 문자열 폭발

# 스택

import sys
from collections import deque

str = list(sys.stdin.readline().strip())
target = list(sys.stdin.readline().strip())

new_str = []
for i in range(len(str)):
  new_str.append(str[i])
  n = len(target)

  # 스택에 쌓인 문자열이 폭발 문자열의 길이보다 클 때
  if len(new_str) >= n:
    search = new_str[-n:]
    if search == target: # 폭발 문자열과 같은지 확인
      for _ in range(n): # 같다면 스택에서 pop
        new_str.pop()

if new_str:
  for str in new_str:
    print(str, end='')
else:
  print('FRULA')