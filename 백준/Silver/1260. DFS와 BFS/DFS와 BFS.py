import sys
from collections import deque

def dfs(adjList, root): # 스택
  stack = deque([root])
  visited = set()

  while stack:
    v = stack.pop()
    if v not in visited:
      visited.add(v)
      print(v, end=' ')
      stack.extend(reversed(sorted(adjList[v]))) # 방문할 수 있는 정점이 여러 개인 경우 작은 것부터

def bfs(adjList, root):
  queue = deque([root])
  visited = set()

  while queue:
    v = queue.popleft()
    if v not in visited:
      visited.add(v)
      print(v, end=' ')
      queue.extend(sorted(adjList[v]))  # 방문할 수 있는 정점이 여러 개인 경우 작은 것부터

N, M, V = map(int, sys.stdin.readline().split())
# 인접 리스트 초기화
adjList = {i: [] for i in range(1, N+1)}

# 간선 추가
for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  adjList[a].append(b)
  adjList[b].append(a)

dfs(adjList, V)
print()
bfs(adjList, V)