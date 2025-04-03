# DP 연습
# 2xn 타일링

import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1) # n = 1일 경우를 대비해서 여유있게 선언
# 0 인덱스부터 사용한다.
dp[0] = 1 # n = 1(idx: 0) → 1
dp[1] = 2  # n = 2(idx: 1) → 2

for i in range(2, N):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[N-1] % 10007)