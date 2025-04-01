import sys

def floyd_warshall(lst):
  for i in range(1, n+1): # 거치는 정점
    for j in range(1, n+1): # 시작하는 정점
      for k in range(1, n+1): # 도착하는 정점
        if lst[j][k] > lst[j][i] + lst[i][k]:
          lst[j][k] = lst[j][i] + lst[i][k]
  return lst

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
INF = float('inf')
fw = [[INF]*(n+1) for _ in range(n+1)] # 1번부터 시작

for _ in range(m):
  i, j, cost = map(int, sys.stdin.readline().strip().split())
  fw[i][j] = min(fw[i][j], cost) # 중복 간선 처리
for i in range(1, n+1):
  fw[i][i] = 0 # 자기 자신은 0으로 초기화

result = floyd_warshall(fw)
for i in range(1, n+1):
  for j in range(1, n+1):
    if result[i][j] == INF: 
      print(0, end=' ')
    else:
      print(result[i][j], end=' ')
  print()
