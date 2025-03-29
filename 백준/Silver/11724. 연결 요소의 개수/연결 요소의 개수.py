import sys
from collections import deque

def dfs(root): # 스택
  stack = deque([root])
  while stack:
    v = stack.pop()
    if v not in visited:
      visited.add(v)
      stack.extend(reversed(adjList[v]))

N, M = map(int, sys.stdin.readline().split())
# 인접 리스트 초기화
adjList = {i: [] for i in range(1, N+1)}
vertexs = [i for i in range(1, N+1)]
visited = set()

# 간선 추가
for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  adjList[a].append(b)
  adjList[b].append(a)

cnt = 0
for v in vertexs:
  if v not in visited:
    dfs(v)
    cnt += 1
print(cnt)