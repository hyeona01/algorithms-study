import sys
from collections import deque

# 빙산을 녹이는 함수
def melt_ice():
  melt = [[0]*M for _ in range(N)]

  for r in range(N):
    for c in range(M):
      if arr[r][c] > 0: # 얼음이 있다면
        cnt = 0
        for i in range(4):
          nx = r + dx[i]
          ny = c + dy[i]
          if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0:
              cnt += 1 # 인접한 영역이 물일 때 높이 1씩 녹음
        melt[r][c] = cnt # 총 녹은 얼음의 높이

  for r in range(N):
    for c in range(M):
      arr[r][c] = max(0, arr[r][c] - melt[r][c]) # 얼음 녹이기

# 빙산의 구역을 세는 함수
def count_ice():
  visited = [[False] * M for _ in range(N)]
  ice_count = 0
  for r in range(1, N-1):
    for c in range(1, M-1):
      if not visited[r][c] and arr[r][c] > 0:
        visited = bfs(visited, r, c)
        ice_count += 1
        if ice_count > 1:
          return 2 # 구역이 두개임
  return ice_count # 구역이 없거나 하나

# bfs
def bfs(visited, r, c):
  queue = deque([(r, c)])
  visited[r][c] = True
  
  while queue: # 인접한 모든 노드 탐색
    row, col = queue.popleft()

    for i in range(4):
      nx = row + dx[i]
      ny = col + dy[i]
      if arr[nx][ny] > 0 and not visited[nx][ny]: # 얼음이라면
        queue.append((nx, ny)) # 큐에 추가
        visited[nx][ny] = True
  return visited

N, M = map(int,sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
for r in range(N):
  arr.append(list(map(int, sys.stdin.readline().strip().split())))

# 메인 함수
time = 0
while True:
  cnt = count_ice()
  if cnt > 1:
    print(time)
    break
  elif cnt == 0:
    print(0)
    break

  melt_ice()
  time += 1