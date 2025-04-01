import sys
from collections import deque

# BFS
# 홍수가 퍼진 영역을 시간 별로 기록 (음수로 시간을 기록)
# 홍수 기록을 바탕으로 고슴도치가 홍수가 퍼지지 않은 곳으로 시간 별로 이동 (양수로 시간을 기록)

R, C = map(int, sys.stdin.readline().split())

INF = float('inf')
move = [[0] * C for _ in range(R)] # 홍수 진행 상태와 고슴도치의 이동 상황 저장
# move = [[INF] * C for _ in range(R)] # 홍수 진행 상태와 고슴도치의 이동 상황 저장
rock = [] # 돌 좌표 저장

water = [] # 홍수 시작점
D = 0 # 비버 집 좌표
S = 0 # 고슴도치 이동 시작점

for r in range(R):
  temp = sys.stdin.readline().strip()
  for c in range(len(temp)):
    # 비버
    if temp[c] == 'D':
      D = (r, c)
    # 고슴도치
    elif temp[c] == 'S':
      S = (r, c)
    # 홍수 시작점
    elif temp[c] == '*':
      water.append((r, c))
    # 돌 위치
    elif temp[c] == 'X':
      rock.append((r,c))

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1] # 상하좌우

def is_rock(x, y): # 돌 위치인지 확인 
  for rock_x, rock_y in rock:
    if x == rock_x and y == rock_y:
      return False
  return True

def is_beaver(x, y): # 비버 위치인지 확인
  if x == D[0] and y == D[1]:
    return False
  return True

# ---- 홍수 ----
queue = deque()
for r, c in water:
  queue.append((r, c))
  move[r][c] = -1 # 시작점 -1

while queue:
  r, c = queue.popleft()

  for i in range(4):
    nx = r + dx[i]
    ny = c + dy[i]
    # 범위 내
    if 0<=nx<R and 0<=ny<C:
      if is_rock(nx, ny) and is_beaver(nx, ny) and move[nx][ny] >= 0: # 가능한 곳 중, 아직 홍수 전인 곳만
        queue.append((nx, ny))
        move[nx][ny] = move[r][c] - 1
  # print(f'홍수 번졌다! {forest}')
  # print(f'홍수 큐 {queue}')

# ---- 고슴도시 ----
target = deque()
target.append(S)
move[S[0]][S[1]] = 1 # 고슴도치 출발

while target:
  # 고슴도치 이동
  t_r, t_c = target.popleft()
  for i in range(4):
    t_nx = t_r + dx[i]
    t_ny = t_c + dy[i]

    if t_nx == D[0] and t_ny == D[1]: # 비버 집에 도착하면 종료
      print(move[t_r][t_c])
      exit()

    if 0<=t_nx<R and 0<=t_ny<C:
      # 돌이 없고, 아직 방문하지 않았고, 홍수가 퍼지지 않은 영역으로 이동 가능
      if is_rock(t_nx, t_ny) and move[t_nx][t_ny] <= 0 and (move[t_nx][t_ny] == 0 or -(move[t_nx][t_ny]) > move[t_r][t_c] + 1):
        move[t_nx][t_ny] = move[t_r][t_c] + 1
        target.append((t_nx, t_ny))
  # print(f'고슴도치 이동! {move}')
  # print(f'도치 큐 {target}')

print('KAKTUS') # 비버 집에 못감 ㅠㅠ