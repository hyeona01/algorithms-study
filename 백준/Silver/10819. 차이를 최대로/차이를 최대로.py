import sys

# key: 재귀함수를 활용하여 브루트 포스 완전 탐색을 해보자.
#      입력 값이 3 ~ 8로 작은 값이기 때문이다.

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0 # 각 요소의 차의 합계를 저장하고 최종적으로 최댓값을 저장하는 변수
visited = [False] * N # 각 자릿수가 선택되었는지 저장하는 배열
perm = [] # 비교할 여러 수열을 저장하는 배열

# 각 인덱스 간의 차의 합을 구하는 함수
def calculate_difference(lst):
  sum = 0
  for i in range(len(lst)-1):
    sum += abs(lst[i] - lst[i+1])
  return sum

# 모든 경우의 배열 조합을 계산해보면 된다! - 재귀함수
def solution(depth):
  global answer

  # 종료 조건: N개의 자릿수가 중복없이 전부 선택되어 list를 이루면 종료 후, 비교
  if depth == N:
    answer = max(calculate_difference(perm), answer)
  
  for i in range(N): # 첫 번째 자리의 경우의 수는 N개
    # 선택되지 않은 값을 확인하고 선택하는 과정
    if visited[i] == False:
      visited[i] = True
      # nums 배열의 i번째 요소 선택
      perm.append(nums[i])
      solution(depth + 1)
      # 비교가 완료되었으면 선택한 요소를 해제하며 False로 변경/비교배열(perm)에서도 삭제해줌.
      # False로 변경된 요소를 통해 또다시 재귀 순환하도록 함.
      visited[i] = False
      perm.pop()

solution(0)
print(answer)