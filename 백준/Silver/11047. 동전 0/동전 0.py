n, k = map(int, input().split())

coins = []
for _ in range(n):
  coins.append(int(input()))
coins.sort(reverse=True)

cnt = 0
for coin in coins:
  if k>=coin:
    cnt += k//coin
    k %= coin
    if k<=0:
      break
# for i in range(len(coins)-1,0,-1):
#   if k>=coins[i]:
#     cnt += k//coins[i]
#     k %= coins[i]
#     if k<=0:
#       break

print(cnt)