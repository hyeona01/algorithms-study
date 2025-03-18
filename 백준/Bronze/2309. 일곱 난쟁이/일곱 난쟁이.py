import sys

heights = [int(sys.stdin.readline()) for _ in range(9)]
fake_min = 0 # 거짓 난쟁이 중 작은 값의 인덱스
fake_max = 8 # 거짓 난쟁이 중 큰 값의 인덱스


# 오름차순으로 정렬한다.
heights.sort()

while True:
  current_sum = 0

# fake_min, fake_max를 제외하고 더하여 본다.
  for i in range(9):
    if i == fake_max or i == fake_min:
      continue
    current_sum += heights[i]

  if current_sum == 100:
    break

# 100 보다 작다면 작은 수를 차례로 배제해본다.
  elif current_sum < 100:
    fake_max -= 1

# 100 보다 크다면 큰 수를 차례로 배제해본다.
  else:
    fake_min += 1

for i in range(9):
  if i == fake_max or i == fake_min:
    continue
  print(heights[i])