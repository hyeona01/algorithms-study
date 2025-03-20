# 부분수열의 합
# 조합 문제임 - 부분수열의 원소가 1~N개일 때의 모든 경우를 완탐

import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, N+1): # 부분 수열의 원소 개수가 1 ~ N까지
  combi = list(combinations(A, i))
  for perm in combi:
    if sum(perm) == S:
      count += 1
print(count)

# visited = [False] * N
# temp = []

# def solution(perm, n):
#   global count

#   if sum(perm) == 0 and len(perm) == n and len(perm) > 0: # 부분수열의 합이 0이고, 부분수열의 원소 수가 n일 경우
#     count += 1
#     return
  
#   for i in range(1, N+1): # 부분수열 원소의 수
#     for idx in range(N):
#       if len(temp) < i - 1 and visited[idx] == False:
#         temp.append(A[idx])
#         visited[idx] = True

#         solution(perm, i)

#         temp.pop()
#         visited[idx] = False

# solution(temp, 0)