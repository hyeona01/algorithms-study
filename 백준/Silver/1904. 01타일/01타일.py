import sys

# 점화식
# D[i] = D[i-1] + D[i-2]
n = int(sys.stdin.readline())
if n == 1:
  print(1)
  exit()

dp = [0] * n
dp[0] = 1
dp[1] = 2

for i in range(2, n):
  dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 모듈러 분배 법칙

print(dp[n-1] % 15746)