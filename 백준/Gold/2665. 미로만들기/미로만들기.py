import sys
import heapq

N = int(sys.stdin.readline())
D = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 흰 방은 비용 0, 검은 방은 비용 1
for _ in range(N):
  temp = list(sys.stdin.readline().rstrip())
  for i in range(N):
    if temp[i] == '0': temp[i] = 1
    else: temp[i] = 0
  D.append(temp)

# 다익스트라 - 우선순위큐
def dijkstra(r, c):
  INF = float('inf')
  cost = [[INF] * N for _ in range(N)]
  visited = [[False] * N for _ in range(N)]
  pq = []
  
  heapq.heappush(pq, (0, r, c)) # 비용, 좌표
  cost[0][0] = 0

  while pq:
    while pq:
      c, x, y = heapq.heappop(pq)
      if not visited[x][y]: # 이미 방문하였으면 제거
        break
    else: # 제거한 후에 더이상 갈 곳이 없다면 완료
      break
    visited[x][y] = True
    
    for i in range(4):
      ny, nx = dy[i] + y, dx[i] + x
      if 0 <= ny < N and 0 <= nx < N:
        new_cost = c + D[nx][ny]
        if cost[nx][ny] > new_cost:
          cost[nx][ny] = new_cost
          heapq.heappush(pq, (new_cost, nx, ny))
  return cost[N-1][N-1] # 오른쪽 아래 방까지의 최소 비용

# print(D)
print(dijkstra(0, 0))