import sys

N = int(sys.stdin.readline())
matrix = []
dp = [[0] * N for _ in range(N)]
INF = float('inf')

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  matrix.append((a, b))


for diff in range(1, N):
  for i in range(N - diff):
    j = i + diff

    if diff == 1: # 행렬간 거리가 1이라면 단순 곱을 해주면 됨
      dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1] # i의 행(N), j의 행(M)과 열(K)
      continue
    dp[i][j] = INF # 최솟값을 구하기 전 초기화
    for k in range(i, j):
      dp[i][j] = min(dp[i][j], (dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]))

print(dp[0][N-1]) # 0번째 행렬과 마지막 행렬곱의 연산 횟수