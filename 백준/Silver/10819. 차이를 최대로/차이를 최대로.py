# 복습

import sys

# 차이를 최대로
# 배열의 순서를 적절히 바꾸는 문제
# 순열 문제이지만 DFS로도 풀 수 있음

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
visited = [False] * n
temp = []
result = 0

def dfs(num):
  global result

  if num == n: # 전체 원소를 추가하면 종료
    diff = 0
    for i in range(1, n):
      diff += abs(temp[i] - temp[i-1]) # 차는 반드시 절대값으로
    result = max(result, diff)
    return result

  for i in range(n): # n개의 원소를 순서를 바꿔가며 첫 원소로 추가해보아야 함
    if not visited[i]:
      visited[i] = True
      temp.append(nums[i])
      dfs(num + 1)
      visited[i] = False
      temp.pop()

dfs(0)
print(result)