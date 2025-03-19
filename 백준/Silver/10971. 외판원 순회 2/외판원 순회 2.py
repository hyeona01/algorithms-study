# 복습

import sys

# 외판원 순회 2 - TSP
# n개의 도시를 중복 없이 순회하고 다시 출발 도시로 돌아온다.
# 행렬로 i에서 j로 이동하는 비용을 주어준다.
# 가장 비용이 적은 루트의 비용을 출력한다.

n = int(sys.stdin.readline())
w = []
visited = [False] * n
visited[0] = True # 0번 도시를 출발 도시로 정한다.
route = [0] # 도시의 인덱스를 저장
min_expense = float('inf')

for i in range(n):
  w.append(list(map(int, sys.stdin.readline().split())))

def tsp(city):
  global min_expense

  if city == n:
    if w[route[-1]][0] != 0:
      expense = 0
      for i in range(n-1):
        expense += w[route[i]][route[i+1]]
      expense += w[route[-1]][0] # 0번 도시로 돌아가는 비용 추가
      min_expense = min(min_expense, expense)
      return
  
  for i in range(1, n): # 0번 도시로 시작하는 것은 고정되었기 때문
    if visited[i] == False:
      if w[route[-1]][i] != 0:
        visited[i] = True
        route.append(i)
        tsp(city + 1)
        visited[i] = False
        route.pop()

tsp(1)
print(min_expense)
