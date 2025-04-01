import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

indegree = [0] * (N+1)
adj_list = {i: [] for i in range(1, N+1)} # 인접 리스트
need = [{} for _ in range(N+1)] # 각 부품 별로 필요한 기본 부품 수

for _ in range(M):
  a, b, amount = map(int, sys.stdin.readline().split())
  adj_list[b].append((a, amount))
  indegree[a] += 1

queue = deque()
for i in range(1, N+1):
  if indegree[i] == 0: # 진입 차수가 0이면 기본 부품
    queue.append(i)

while queue:
  node = queue.popleft()

  for next, amount in adj_list[node]:
    if not need[node]: # 삭제한 노드가 기본 부품이라면
      need[next][node] = amount
    else: # 중간 부품이라면
      for key in need[node]:
        if key in need[next]:
          need[next][key] += need[node][key] * amount
        else:
          need[next][key] = need[node][key] * amount

    # 진입 차수 감소 후 0이 되면 큐에 추가
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)

for key in sorted(need[N].keys()):
  print(key, need[N][key])