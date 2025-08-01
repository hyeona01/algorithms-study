import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, -1, -1, 1, 1]

# 방문 거리 배열
dist = [[-1] * m for _ in range(n)]
q = deque()

# 모든 상어 위치에서 BFS 시작
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0  # 상어 있는 곳은 거리 0

# BFS
while q:
    x, y = q.popleft()
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, dist[i][j])

print(result)