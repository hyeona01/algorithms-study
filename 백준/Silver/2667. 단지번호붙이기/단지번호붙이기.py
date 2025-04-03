import sys
from collections import deque

# BFS
# 1(집이 있는 곳)을 만나면 상하좌우를 살피고 1인 좌표를 큐에 추가
# 큐가 빌 떄까지 각 집을 방문처리
# 모든 행렬을 다 봐야 함

N = int(sys.stdin.readline())
apt = []
for _ in range(N):
  apt.append(list((sys.stdin.readline().strip()))) # 문자열 0, 1로 처리

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def BFS(r, c): # 값이 1인 것만 받을 예정
  queue = deque()
  queue.append((r, c))
  visited[r][c] = True
  cnt = 1 # 단지내 집의 수
  
  while queue:
    cur_r, cur_c = queue.popleft()
    for i in range(4):
      nx = cur_r + dx[i]
      ny = cur_c + dy[i]
      if 0 <= nx < N and 0 <= ny < N: # 범위 내
        if not visited[nx][ny] and apt[nx][ny] == '1': # 아직 방문하지 않은 집이라면
          queue.append((nx, ny)) # 인접한 집 큐에 추가
          visited[nx][ny] = True
          cnt += 1
  return cnt # 인접한 모든 집의 수
  # return cnt if cnt > 1 else 0 # 인접한 모든 집의 수

# 메인 실행문
result = []
visited = [[False] * N for _ in range(N)]
for row in range(N):
  for col in range(N):
    if not visited[row][col] and apt[row][col] == '1':
      cnt = BFS(row, col)
      if cnt > 0:
        result.append(cnt)

print(len(result))
result.sort()
for r in result:
  print(r)
# print(result)