import sys
from collections import deque

# bfs - 특정 거리
def bfs(x, distance):
  queue = deque([(0, x)]) # 레벨, 값
  visited = set()
  result = []

  while queue:
    level, v = queue.popleft()

    if v not in visited:
      visited.add(v)
      if distance == level:
        result.append(v)
      for edge in edges[v]:
        queue.append((level + 1, edge))
  return result
  
N, M, K, X = map(int,sys.stdin.readline().split())
edges = {i: [] for i in range(1, N+1)}

for _ in range(M):
  a, b = map(int,sys.stdin.readline().split())
  edges[a].append(b)

nodes = sorted(bfs(X, K))
if not nodes:
  print(-1)
for node in nodes:
  print(node)