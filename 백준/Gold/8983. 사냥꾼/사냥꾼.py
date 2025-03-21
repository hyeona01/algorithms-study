import sys

M, N, L = map(int, sys.stdin.readline().split())
hunters = list(map(int, sys.stdin.readline().split()))
animals = []
hunters.sort()

for i in range(N):
  animals.append(list(map(int, sys.stdin.readline().split())))

def binary_search(lst, a_x): # 동물의 x좌표와 가장 인접한 hunter 찾기
  result = 0
  left = 0
  right = len(lst) - 1

  while left <= right:
    mid = (left+right) // 2
    if a_x >= hunters[mid]:
      result = mid
      left = mid + 1
    elif a_x < hunters[mid]:
      right = mid - 1
  return result

count = 0
for i in range(N): # 동물들마다 순회
  a_x = animals[i][0]
  a_y = animals[i][1]
  # y 값은 L에 의존되지만, x값은 이분탐색으로 효율적으로 찾을 수 있음(가장 가까운 x값을 찾고, 그 x값이 범위 안에 있는지 확인하면 됨)
  if 0 <= a_y <= L:
    # 동물과 x값이 가까운 사대를 찾음
    idx = binary_search(hunters, a_x)
    # 발견한 idx-1, idx, idx+1 모두 가장 가까울 가능성 있음
    for i in range(idx-1, idx+2):
      if 0 <= i < M:
        if abs(a_x-hunters[i]) < abs(a_x-hunters[idx]):
          idx = i
    # 가장 가까운 idx 사대에서 사냥이 가능한지 확인
    if L-a_y >= abs(hunters[idx]-a_x):
      count += 1

print(count)