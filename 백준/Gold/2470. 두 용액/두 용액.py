import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

# 0에 가까운 두 용액

# -- key point --
# start와 end의 합이 0보다 크다 -> 너무 양수 쪽이다. 음수 쪽(좌)로 이동
# start와 end의 합이 0보다 작다 -> 너무 음수 쪽이다. 양수 쪽(우)로 이동

start = 0
end = N-1
result = float('inf')
a = 0 # 작은 수의 용액
b = 0 # 큰 수의 용액

while start < end: # 투 포인터이고 1씩 값이 변화하기 때문에 <= 을 하게 되면 연산을 한 번 더 하게 됨
  center = (start + end) // 2
  diff = arr[start] + arr[end]

  if diff >= 0:
    if result > abs(diff):
      a = arr[start]
      b = arr[end]
      result = abs(diff)
    end = end - 1
  
  elif diff < 0:
    if result > abs(diff):
      a = arr[start]
      b = arr[end]
      result = abs(diff)
    start = start + 1

print(a, b)
# print(result)