import sys
from collections import deque

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
arr = [[False]*N for _ in range(N)]
directions = []
time = 0
x, y = 0, 0 # snake 좌표
snake = deque([[x, y]]) # [x, y]

for i in range(K):
  r, c = map(int, sys.stdin.readline().split())
  arr[r-1][c-1] = True # 시작점을 0,0 기준으로 설정함

L = int(sys.stdin.readline().strip())
for dir in range(L):
  t, d = map(str, sys.stdin.readline().strip().split())
  directions.append([int(t), d])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0 # 방향 초기화(우측)
chang_dir_idx = 0

while True:
  time += 1

  # 이동
  x = snake[-1][0] + dx[dir]
  y = snake[-1][1] + dy[dir]

  # 뱀이 벽에 닿음
  if not (0 <= x < N and 0 <= y < N):
    break 
  # 자기 몸에 닿음
  if [x, y] in snake:
    break

  # snake 큐에 추가
  snake.append([x, y])

  # 사과 여부
  if 0 <= x < N and 0 <= y < N:
    if not arr[x][y]: # 사과에 닿지 않음
      snake.popleft()
    else: arr[x][y] = False # 사과 없앰

  # 방향 전환 여부
  if chang_dir_idx < L and directions[chang_dir_idx][0] == time:
    if directions[chang_dir_idx][1] == 'D': # 오른쪽으로 회전
      dir = (dir + 1) % 4
    else: # 왼쪽으로 회전
      dir = (dir - 1) % 4
    chang_dir_idx += 1

print(time)