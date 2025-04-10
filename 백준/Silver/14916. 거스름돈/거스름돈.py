import sys

n = int(sys.stdin.readline())
INF = float('inf')
dp = [INF] * (n+1)
dp[0] = 1

for coin in (2, 5):
  for i in range(coin, n + 1):
    dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[n] == INF:
  print(-1)
else:
  print(dp[n] - 1)