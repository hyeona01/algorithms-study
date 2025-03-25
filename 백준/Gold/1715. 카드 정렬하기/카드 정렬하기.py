import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
  heapq.heappush(arr, int(sys.stdin.readline().strip()))

result = 0
# 가장 작은 묶음을 두개 선택해서 합쳐나가야 함
while len(arr) > 1:
  current = heapq.heappop(arr) + heapq.heappop(arr)
  result += current
  heapq.heappush(arr, current)

print(result)