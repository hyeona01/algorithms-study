import sys

N = int(sys.stdin.readline())

num_dict = {}

for i in range(N):
  num = int(sys.stdin.readline())

  if num in num_dict: # 기존에 존재하는 숫자라면
    num_dict[num] += 1 # value 증가
  else:
    num_dict[num] = 1 # 기존에 존재하지 않는 숫자라면 추가

for i in range(len(num_dict)):
  # dictionary의 key 값 중 가장 작은 key 찾기
  min_key = min(num_dict.keys())
  value = num_dict.get(min_key)

  for j in range(value):
    print(min_key)
  
  # min 삭제
  num_dict.pop(min_key)