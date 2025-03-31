import sys

# N이 2 ~ 11 사이의 값이므로 DFS로 풀기
def operate(a, b, o):
  if o == 0: # 더하기
    return a + b
  elif o == 1: # 빼기
    return a - b
  elif o == 2: # 곱하기
    return a * b
  else: # 나누기
    if a < 0:
      return -(-a // b) # 음수일 경우 처리
    return a // b

def dfs(visited, lst, current_max, current_min):
  if len(lst) == N-1: # 모든 연산자의 순서가 정해지면
    a = nums[0]
    for i in range(N-1):
      a = operate(a, nums[i+1], lst[i])
    current_max = max(current_max, a)
    current_min = min(current_min, a)
    return current_max, current_min
  
  for i in range(4):
    if visited[i] > 0:
      visited[i] -= 1
      lst.append(i) # 연산자 추가
      current_max, current_min = dfs(visited, lst, current_max, current_min) # 재귀호출
      visited[i] += 1
      lst.pop() # 연산자 제거
  return current_max, current_min

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 0: plus, 1: minus, 2: multi, 3: divide
operators = list(map(int, sys.stdin.readline().split()))
visited = operators[:] # 복사

minimum = float('inf')
maximum = -float('inf')

maximum, minimum = dfs(visited, [], maximum, minimum)
print(maximum)
print(minimum)