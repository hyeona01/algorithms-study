import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
  for j in range(i):
    if lst[j] >= (i - j): # 떨어진 거리보다 점프 수가 같거나 크다면
      dp[i] = min(dp[j] + 1, dp[i])

if dp[n-1] != float('inf'):
  print(dp[n-1])
else:
  print(-1)