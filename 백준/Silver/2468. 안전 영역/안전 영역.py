# 복습

import sys
sys.setrecursionlimit(10000)

# 안전영역
# 잠길 수 있는 영역은 0부터 가장 높은 높이 -1
# DFS를 사용해서 인접한 지역을 재귀적으로 탐색 -> 탐색이 종료되면 return 1
# 전체 행, 열을 순회하여 return 받을 때마다 count 를 올려줌

n = int(sys.stdin.readline())
area = []
max_height = 0
max_safe_cnt = 0

dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [-1, 1, 0, 0] # 상 하 좌 우

for i in range(n):
  lst = list(map(int, sys.stdin.readline().split()))
  area.append(lst)
  max_height = max(max_height, max(lst))

# 해당 높이보다 높은 좌표는 안전 영역으로 표시하는 함수
def dfs(height, r, c, visited):
  # 인접한 상하좌우 깊이 탐색(DFS)
  for i in range(4):
    nx = r+dx[i]
    ny = c+dy[i]
    if 0 <= nx < n and 0 <= ny < n: # 유효한 경로인지 검증
      if not visited[nx][ny] and area[nx][ny] > height:
        visited[nx][ny] = True
        dfs(height, nx, ny, visited)

# 침수 높이를 0부터 max-1까지 순회하며 탐색
for h in range(0, max_height):
  visited = [[False] * n for _ in range(n)] # 잠기지 않는 지역을 표시하는 2차원 배열
  count = 0
  for i in range(n): # 행
    for j in range(n): # 열
      if not visited[i][j] and area[i][j] > h: # 아직 방문 전이라면
        visited[i][j] = True # 방문하고
        dfs(h, i, j, visited) # 인접 지역 방문
        count += 1
  max_safe_cnt = max(max_safe_cnt, count)

print(max_safe_cnt)
