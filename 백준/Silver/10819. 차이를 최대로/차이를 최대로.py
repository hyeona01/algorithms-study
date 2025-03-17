import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0
visited = [False]*N

def calculate_difference(lst):
  sum = 0
  for i in range(len(lst)-1):
    sum += abs(lst[i] - lst[i+1])
  return sum

# 모든 경우의 수를 구해보자. N!
# 입력 값이 3 ~ 8로 작은 값이기 때문이다.

# 모든 경우의 리스트 조합을 계산해보면 된다! - 재귀함수
def solution(list):
  global answer
  # 종료 조건: N개의 자릿수가 중복없이 전부 선택되어 list를 이루면 종료 후, 비교
  if len(list) == N:
    answer = max(calculate_difference(list), answer)
  
  for i in range(N): # 첫 번째 자리의 경우의 수는 N개
    # 선택되지 않은 값을 확인하고 선택하는 과정
    if visited[i] == False:
      visited[i] = True
      # nums 배열의 i번째 요소 선택
      list.append(nums[i])
      solution(list)
      # 비교가 완료되었으면 선택한 요소를 해제하며 False로 변경해줌.
      # False로 변경된 요소를 통해 또다시 재귀 순환하도록 함.
      visited[i] = False
      list.pop()

solution([])
print(answer)