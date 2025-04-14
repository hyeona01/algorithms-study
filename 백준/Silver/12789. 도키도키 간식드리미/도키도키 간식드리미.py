import sys
from collections  import deque

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
temp = deque() # 임시보관 스택

current = 1 # 다음에 와야할 번호표
i = 0 # 현재 arr 인덱스

while i < N:
  if arr[i] > current:
    temp.append(arr[i])
    i += 1
    continue

  elif arr[i] == current:
    current += 1
    i += 1
    while temp and temp[-1] == current:
      current += 1
      temp.pop()

if i != N or temp:
  print('Sad')
else:
  print('Nice')