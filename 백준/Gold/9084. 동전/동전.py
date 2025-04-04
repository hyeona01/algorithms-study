import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  coin_list = list(map(int, sys.stdin.readline().split()))
  M = int(sys.stdin.readline())

  dp = [0] * (M + 1)
  dp[0] = 1 # 0원을 만드는 경우는 늘 하나
  
  for c in coin_list: # 동전 종류마다 만들 수 있는 경우의 수 업데이트
    for i in range(c, M + 1):
      dp[i] += dp[i-c]

  print(dp[M])