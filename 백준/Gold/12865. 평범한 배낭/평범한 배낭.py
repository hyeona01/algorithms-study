import sys

N, K = map(int, sys.stdin.readline().split())
items = []
for _ in range(N):
  w, v = map(int, sys.stdin.readline().split())
  items.append((w, v))

dp = [0] * (K+1) # 해당 무게에서 가지는 최대 가치합

for w, v in items:
  # 적은 금액부터 가치를 채우다보면 금액이 가치의 두배가 되는 순간부터 중복되기에 이를 방지하기 위해 뒤부터
  for i in range(K, w - 1, -1): 
    if dp[i-w] + v > dp[i]:
      dp[i] = dp[i-w] + v

print(dp[-1])
# print(dp)