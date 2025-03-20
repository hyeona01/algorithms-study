import sys
import time

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target_nums = list(map(int, sys.stdin.readline().split()))

def binary_search(num_list, target):
  pl = 0
  pr = len(num_list) - 1

  while True:
    pc = (pl + pr) // 2

    # 더이상 범위를 좁힐 수 없음
    if pr < pl:
      return 0
    
    # 탐색 성공
    if target == num_list[pc]:
      return 1
    
    # 우측으로 범위 좁힘
    elif target > num_list[pc]:
      pl = pc + 1
    
    # 좌측으로 범위 좁힘
    else:
      pr = pc - 1

start_time = time.time() # 시간 측정

nums.sort() # 정렬

for key in target_nums: # 이진 검색
  print(binary_search(nums, key))

end_time = time.time()
# print(f'{end_time - start_time:.5f} sec')
# 0.00011 sec