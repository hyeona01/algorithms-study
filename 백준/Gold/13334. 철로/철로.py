import sys
import heapq

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  arr.append((min(a, b), max(a, b)))

arr.sort(key=lambda x: (x[1])) # 끝점을 기준으로 정렬

d = int(sys.stdin.readline().strip())
result = 0
temp = [] # 특정 철로에 포함되는 사람들의 시작점 배열

for i in range(len(arr)):
  end = arr[i][1] # 끝점 선택
  start = end - d # 시작점 설정

  heapq.heappush(temp, arr[i][0]) # 현재 선분의 시작점 추가

  while temp and temp[0] < start:
    heapq.heappop(temp)

  result = max(result, len(temp))

print(result)