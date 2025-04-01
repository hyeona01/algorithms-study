import sys
from collections import deque

# BFS

M, N, H = map(int, sys.stdin.readline().split())
# 0: 안 익음 1: 익음 -1: 없음
box = [] # 토마토 상태를 담음

dh = [1, -1, 0, 0, 0, 0] # 위, 아래, 앞, 뒤, 좌, 우
dx = [0, 0, -1, 1, 0, 0] # 위, 아래, 앞, 뒤, 좌, 우
dy = [0, 0, 0, 0, -1, 1] # 위, 아래, 앞, 뒤, 좌, 우

# 익은 토마토만 따로 관리(동시에 인접 토마토를 익게 해야 하기에
queue = deque()

for h in range(H):
  temp = []
  for r in range(N):
    tomato = list(map(int, sys.stdin.readline().split()))
    for i in range(len(tomato)):
      if tomato[i] == 1:
        queue.append((h, r, i)) # 익은 토마토 좌표
    temp.append(tomato)
  box.append(temp)

# 입력 받을 때 모든 토마토가 익어있는 상태라면 0 출력
if len(queue) == M*N*H:
  print(0)
  exit()

# BFS 순회
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
while queue:
  st_h, st_row, st_col = queue.popleft()
  # 방문 처리
  if visited[st_h][st_row][st_col]:
    continue
  else:
    visited[st_h][st_row][st_col] = True

  for i in range(6):
    nh = st_h + dh[i]
    nx = st_row + dx[i]
    ny = st_col + dy[i]

    if 0<=ny<M and 0<=nx<N and 0<=nh<H:
      if box[nh][nx][ny] == 0: # 익지 않은 토마토 일 때
        box[nh][nx][ny] = box[st_h][st_row][st_col] + 1 # 이전 토마토가 익은 시간 + 1
        queue.append((nh, nx, ny))

# 모든 토마토가 익지 못하면 -1 출력(box 중 0이 남아있다면)
# 모든 토마토가 익었다면 날짜 출력
result = 0
for i in range(H):
  for j in range(N):
    result = max(result, max(box[i][j][:]))
    if 0 in box[i][j][:]:
      print(-1)
      exit()
print(result - 1) # 시작 날짜가 1이었기 때문