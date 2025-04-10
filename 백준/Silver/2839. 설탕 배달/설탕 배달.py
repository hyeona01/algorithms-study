import sys
N = int(sys.stdin.readline().strip())

INF = float('inf')
dp = [INF] * (N+1)
dp[0] = 0

for kg in (3, 5):
  for i in range(kg, N+1):
    dp[i] = min(dp[i], dp[i-kg] + 1)

if dp[N] == INF:
  print(-1)
else:
  print(dp[N])
