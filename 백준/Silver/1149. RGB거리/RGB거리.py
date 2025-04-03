# DP 연습
# RGB 거리

import sys

N = int(sys.stdin.readline())
rgb = []
for _ in range(N):
  rgb.append(list(map(int, sys.stdin.readline().split())))

INF = float('inf')
dp = [[INF] * N for _ in range(N)]
dp[0][0] = rgb[0][0] # Red
dp[0][1] = rgb[0][1] # Green
dp[0][2] = rgb[0][2] # Black

for i in range(1, N):
  for color in range(3):
    if color == 0: # R
      dp[i][color] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    elif color == 1: # G
      dp[i][color] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    else: # B
      dp[i][color] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[-1]))
