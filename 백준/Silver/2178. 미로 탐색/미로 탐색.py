import sys
from collections import deque

# bfs + 큐
def bfs(r, c):
  queue = deque([[r, c]])
  visited = [[False] * M for _ in range(N)]
  visited[r][c] = True
  
  while queue:
    r, c = queue.popleft()

    if r == N-1 and c == M-1:
      return maze[r][c]

    for i in range(4):
      nx = r + dx[i]
      ny = c + dy[i]
      # 다음 레벨의 노드가 1.범위 내에 있고 2.방문하지 않았고 3.갈 수 있는 길이라면 방문한다.
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
        visited[nx][ny] = True
        maze[nx][ny] = maze[r][c] + 1 # 다음 레벨 기록
        queue.append([nx, ny])
  
N, M = map(int,sys.stdin.readline().split())
maze = []
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

for _ in range(N):
  maze.append(list(map(int, sys.stdin.readline().strip())))

# print(maze)
print(bfs(0,0))
# print(maze)