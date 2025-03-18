import sys

N = int(sys.stdin.readline())
W = []
for i in range(N):
  W.append(list(map(int, sys.stdin.readline().split())))

visited = [False] * N
visited[0] = True
travel_city = [0] # 방문한 도시의 인덱스가 순서대로 담긴다.
result = float('inf')

# goal: 도시의 순서를 적절하게 재배치한다.
def travel(city):
  # global N
  # global W
  # global visited
  # global travel_city
  global result

  if city == N:
    # 출발지로 돌아가는 경로가 존재하는지 체크
    if W[travel_city[-1]][0] != 0:
      # 최적 경로의 비용을 계산한다.
      temp = 0

      for i in range(N-1):
        temp += W[travel_city[i]][travel_city[i+1]]
      # 출발지로 돌아가는 비용을 추가한다.
      temp += W[travel_city[-1]][0]
      result = min(result, temp)
    return
  
  for i in range(1, N): # 0번 도시는 이미 방문하였기에 1번 도시부터 위치를 찾기
    # 이전 노드에서 i 노드로 이동할 수 있는지 확인
    if not visited[i] and W[travel_city[-1]][i] != 0: # 아직 방문하지 않았다면 방문하고 비용 계산하기
      travel_city.append(i)
      visited[i] = True
      travel(city + 1)
      visited[i] = False
      travel_city.pop()

travel(1)
print(result)