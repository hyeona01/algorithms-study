import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())
prices = []

# 희망 가격 높은 순
for _ in range(M):
  heapq.heappush(prices, -int(sys.stdin.readline()))

result = 0
price = 0
for possible in range(1, M + 1): # 구입 가능한 사람
  cur = -heapq.heappop(prices)
  if result < cur * possible and possible <= N:
    result = cur * possible
    price = cur

print(price, result)