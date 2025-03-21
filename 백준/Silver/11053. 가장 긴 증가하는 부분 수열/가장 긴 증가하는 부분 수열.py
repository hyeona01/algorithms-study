import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 가장 긴 증가하는 부분 수열
dp = [1] * N # 하나의 원소는 최소 수열의 길이가 1

for i in range(N):
  max_dp = 0
  for j in range(i): # dp[i]를 구하기 위해 0~i까지의 원소와 해당 dp값 확인
    if arr[j] < arr[i] and dp[j] > max_dp: # 조건에 해당하는 원소 중 가장 큰 원소의 인덱스(dp[j])에서 1 더한 수를 dp[i]로 업데이트
      max_dp = max(dp[j], max_dp)
      dp[i] = dp[j] + 1

print(max(dp))
# print(arr)
# print(dp)
