import sys
from collections import deque

# 가로 나무판은 우측의 것들을 모두 True로 바꾸며 count 증가
# 세로 나무판은 아래쪽의 것들을 모두 True로 바꾸며 count 증가

# DFS

N, M = map(int, sys.stdin.readline().split())
woods = []
for _ in range(N):
  woods.append(list(sys.stdin.readline().strip()))
  
def DFS(r, c):
  stack = deque()
  stack.append((r, c, woods[r][c])) # 초기화(행, 열, 나무판자 종류)
  woods_cnt = 0

  while stack:
    cur_r, cur_c, cur_w = stack.pop()
    if visited[cur_r][cur_c]: # 이미 방문했다면 pass
      continue
    
    visited[cur_r][cur_c] = True
    woods_cnt += 1 # 나무 판자 하나 증가

    if cur_w == '-':
      ny = cur_c + 1
      while ny < M: # 범위 내
        if woods[cur_r][ny] == '-': # 동일한 나무판자라면
          visited[cur_r][ny] = True # 방문 처리
          ny += 1
        else: # 동일한 나무판자가 아니면 종료
          break
      if 0 <= ny < c: # 범위 내라면 이어 순회
        stack.append((cur_r, ny, woods[cur_r][ny]))
      else: # 범위를 벗어나면 다음 행 순회
        return woods_cnt
    else: # | 무늬
      nx = cur_r + 1
      while nx < N: # 범위 내
        if woods[nx][cur_c] == '|': # 동일한 나무판자라면
          visited[nx][cur_c] = True # 방문 처리
          nx += 1
        else:
          break
      if 0 <= nx < r: # 범위 내라면 이어 순회
        stack.append((nx, cur_c, woods[nx][cur_c]))

  return woods_cnt

result = 0
visited = [[False]*M for _ in range(N)] # 초기화
for row in range(N):
  for col in range(M):
    result += DFS(row, col)
print(result)