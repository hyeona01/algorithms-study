# 부분수열의 합
# 조합 문제임 - 부분수열의 원소가 1~N개일 때의 모든 경우를 완탐

import sys

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
count = 0

def solution(idx, sum_list):
  global count
  if (idx == 0 and len(sum_list) > 0) or 0 < idx <= N:
  # if idx < N: # 인덱스 범위
    if sum(sum_list) == S: # base case: 합이 S와 일치하는지 확인
      count += 1

  for i in range(idx, N): # 현재 인덱스 이후의 인덱스만 탐색함(중복 제거)
    # if idx == 0 or idx < i: # 직전 인덱스 보다 커야 함(중복 제거)
    sum_list.append(A[i]) # 원소 추가
    solution(i+1, sum_list) # base case 확인
    sum_list.pop()

solution(0, [])
print(count)