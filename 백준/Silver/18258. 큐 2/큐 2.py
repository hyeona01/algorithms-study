import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

def solution(str):
  command = list(str.split())
  
  if command[0] == 'push':
    queue.append(int(command[1]))
  elif command[0] == 'pop':
    if len(queue) > 0: print(queue.popleft())
    else: print(-1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    if len(queue) > 0: print(0)
    else: print(1)
  elif command[0] == 'front':
    if len(queue) == 0: print(-1)
    else: print(queue[0])
  elif command[0] == 'back':
    if len(queue) == 0: print(-1)
    else: print(queue[-1])
  else:
    print('잘못 입력!')

for i in range(N):
  solution(sys.stdin.readline())