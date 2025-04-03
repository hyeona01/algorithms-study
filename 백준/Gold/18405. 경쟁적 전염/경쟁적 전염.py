import sys
from collections import deque

# BFS

N, K = map(int, sys.stdin.readline().strip().split())
arr = []
virus_list = []
for r in range(N):
  temp = list(map(int, sys.stdin.readline().strip().split()))
  arr.append(temp)
  for c in range(N):
    if temp[c] != 0:
      virus_list.append((temp[c], 0, r, c))  # (바이러스 종류, 시간, 행, 열)

S, X, Y = map(int, sys.stdin.readline().strip().split())

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def BFS():
  # 바이러스 번호 낮은 순서로
  virus_list.sort()
  queue = deque(virus_list)

  while queue:
    virus, time, x, y = queue.popleft()
    # S초
    if time == S:
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
        arr[nx][ny] = virus  # 바이러스 전염
        queue.append((virus, time + 1, nx, ny))  # 시간 +1
BFS()
print(arr[X-1][Y-1])

# # 특정 좌표에서 인접한 곳에 바이러스를 전염
# def BFS(r, c, virus):
#   queue = deque()
#   queue.append((r, c))
#   visited[r][c] = True
  
#   # while queue:
#   cur_r, cur_c = queue.popleft()
#   for i in range(4):
#     nx = cur_r + dx[i]
#     ny = cur_c + dy[i]
#     if 0 <= nx < N and 0 <= ny < N: # 범위 내
#       if not visited[nx][ny]: # 아직 방문하지 않았다면
#         visited[nx][ny] = True
#         arr[nx][ny] = virus # 바이러스 전염

# for _ in range(S): # S초
#   for row in range(N):
#     for col in range(N):
#       if visited[row][col]: # 이미 전염되었다면 Pass
#         continue
#       for i in range(1, K+1): # 1번 바이러스부터 k번 바이러스까지
#         if arr[row][col] == i:
#           BFS(row, col, arr[row][col])

# print(arr[X-1][Y-1])