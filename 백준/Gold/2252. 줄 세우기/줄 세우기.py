import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
edges = {i: [] for i in range(1, N+1)}
indegree = [0] * (N+1)

for _ in range(M):
  a, b = map(int,sys.stdin.readline().split())
  edges[a].append(b) # a->b 간선
  indegree[b] += 1 # b의 들어오는 점이 1 추가

queue = deque()
for i in range(1, N+1):
  if indegree[i] == 0: 
    queue.append(i) # indegree가 0이면 큐에 추가

while queue:
  v = queue.popleft()
  print(v, end=' ')
  # 현재 정점와 관계가 있는 정점은 indegree 1 감소
  temp = edges[v]
  for item in temp:
    indegree[item] -= 1
    if indegree[item] == 0:
      queue.append(item)
