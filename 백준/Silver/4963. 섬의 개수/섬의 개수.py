import sys
sys.setrecursionlimit(10**6)

# 상하좌우, 좌측 대각선, 우측 대각선, 우측 하단 대각선, 좌측 하단 대각선
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]

def dfs(r, c, arr):
  for i in range(8):
    nr = r + dx[i]
    nc = c + dy[i]

    if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and arr[nr][nc]:
      visited[nr][nc] = 1
      dfs(nr, nc, arr)

# w, h, arr
def find_land(w, h, arr):
  cnt = 0
  for r in range(h):
    for c in range(w):
      if not visited[r][c] and arr[r][c]: # 방문하지 않았고, 땅이라면
        dfs(r, c, arr)
        cnt += 1
        visited[r][c] = 1
  return cnt

# main
while True:
  w, h = map(int, sys.stdin.readline().split())
  if w == 0 and h == 0:
    break

  arr = []
  for i in range(h):
    arr.append(list(map(int, sys.stdin.readline().split())))

  global visited
  visited = [[0] * w for _ in range(h)]

  print(find_land(w, h, arr))