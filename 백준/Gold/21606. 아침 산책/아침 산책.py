import sys
from collections import deque

N = int(sys.stdin.readline())
A = sys.stdin.readline().strip()
indoor = [None] # 인덱스 1부터 시작
for a in A:
  if a == '0':
    indoor.append(False)
  else:
    indoor.append(True)

adj_list = {i: [] for i in range(1, N+1)}
for i in range(N-1):
  a, b = map(int, sys.stdin.readline().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

def dfs():
  result = 0
  stack = deque()
  for start in range(1, N+1):
    visited = set()
    if not indoor[start]: # 출발점이 실외라면 제외
      continue
    stack.append(start)
    while stack:
      v = stack.pop()
      if v not in visited:
        if indoor[v] and v != start: # 끝점이 실내라면 경우의 수 추가
          result += 1
        else:
          stack.extend(reversed(adj_list[v])) # v가 실외라면 더 순회
        visited.add(v)
  return result

print(dfs())