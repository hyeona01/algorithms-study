import sys
import heapq

N = int(sys.stdin.readline().strip())
min_heap = [] # 루트값 보다 큰 값이 모임 - top은 큰 값 중 가장 작은 값
max_heap = [] # 루트값 보다 작은 값이 모임 - top은 작은 값 중 가장 큰 값(중간값)

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

print(a)
if a > b:
  min_heap.append(a)
  max_heap.append(-b)
else:
  max_heap.append(-a)
  min_heap.append(b)
print(-max_heap[0])

for i in range(N-2):
  x = int(sys.stdin.readline().strip())
  if x > -max_heap[0]: # top 보다 크면
    heapq.heappush(min_heap, x)
  else:
    heapq.heappush(max_heap, -x)

  # max_heap은 늘 min_heap 보다 커야 함. -> 짝수개라면 더 작은 수를 말해야 하기 때문
  # max_heap이 min_heap의 원소 보다 적다면 max_heap으로 옮겨줘야 함
  if len(max_heap) < len(min_heap):
    heapq.heappush(max_heap, -heapq.heappop(min_heap))
  elif len(max_heap) > len(min_heap)+1:
    heapq.heappush(min_heap, -heapq.heappop(max_heap)) 

  print(-max_heap[0])