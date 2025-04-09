import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
adj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = float('inf')

# dp[current][visited]: current 도시에서 visited 상태일 때 남은 도시 모두 방문 후 돌아가는 최소 비용
# 1 << N: N개의 도시를 모두 벙문하였을 때의 비트마스킹
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(current, visited):
  # 모든 도시를 방문했을 경우
  if visited == (1 << N) - 1:
    if adj[current][0] > 0: # 갈 수 있는 길
      return adj[current][0]
    else: 
      return INF

  # 이미 계산된 경우
  if dp[current][visited] != -1:
    return dp[current][visited]

  dp[current][visited] = INF  # 초기값 설정
  for next in range(N):
    # 아직 방문하지 않은 도시이고, 경로가 존재할 때
    if (visited & (1 << next)) == 0 and adj[current][next] > 0:
      # 재귀 매개변수 - 'current': next, 'visited': visited 집합에서 next 도시를 제외
      cost = adj[current][next] + tsp(next, visited | (1 << next))
      dp[current][visited] = min(dp[current][visited], cost)

  return dp[current][visited]

# 0번 도시에서 시작, 0번 도시만 방문한 상태는 visited = 1 (2^0)
print(tsp(0, 1))
# print(dp)