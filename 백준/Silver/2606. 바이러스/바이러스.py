import sys
from collections import deque

def dfs(root): # 스택
  stack = deque([root])
  while stack:
    v = stack.pop()
    if v not in visited:
      visited.add(v)
      stack.extend(reversed(adjList[v]))

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
# 인접 리스트 초기화
adjList = {i: [] for i in range(1, V + 1)}
visited = set()

# 간선 추가
for i in range(E):
  a, b = map(int, sys.stdin.readline().split())
  adjList[a].append(b)
  adjList[b].append(a)

dfs(1)
print(len(visited)-1) # 1번 컴퓨터는 제외함