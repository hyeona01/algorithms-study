import sys

arr = list(map(int, sys.stdin.readline().split()))
n = arr.pop(0)

# 스택으로 풀어보자
def max_square(arr):
  n = len(arr)
  new_stack = []
  result = 0
  current = 0 # 추가하고자 하는 원소 값

  for i in range(n):    
    current = arr[i]
  
    valid_idx = i # pop한 이후 push할 때 index를 수정해주어야 함
    while len(new_stack) > 0:
      if current >= new_stack[-1][1]: # 추가하고자 하는 값이 더 작을 때만 반복
        break
      pop_item = new_stack.pop() # 스택을 pop
      valid_idx = pop_item[0]
      result = max((i-pop_item[0])*pop_item[1], result) # 추가하고자 하는 원소(값이 작은) 인덱스 - 스택에서 pop한 원소(값이 큰) 인덱스 X pop value
    # 스택에 추가(index, value)
    new_stack.append([valid_idx, arr[i]])

  # 남아있는 스택을 전부 pop하면서 넓이 계산
  last_idx = n
  while len(new_stack) > 0:
    pop_item = new_stack.pop() # 스택을 pop
    result = max((last_idx-pop_item[0])*pop_item[1], result)

  return result

# print(max_square(arr))

while n != 0:
  print(max_square(arr))
  arr = list(map(int, sys.stdin.readline().split()))
  n = arr.pop(0)