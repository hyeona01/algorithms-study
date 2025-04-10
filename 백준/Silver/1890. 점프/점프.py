# 53%

import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
  for c in range(N):
    if arr[r][c] == 0 or dp[r][c] == 0:
      continue
    jump = arr[r][c]
    if r + jump < N:
      dp[r + jump][c] += dp[r][c]
    if c + jump < N:
      dp[r][c + jump] += dp[r][c]

print(dp[N-1][N-1])
# for row in dp:
#   print(row)