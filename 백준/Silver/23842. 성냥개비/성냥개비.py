import sys

N = int(sys.stdin.readline().strip()) - 4 # 연산자 성냥 개수 제외
counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] # 0 ~ 9까지 필요한 성냥 개수

for a in range(10):
  if counts[a] >= N:
    continue
  for b in range(10):
    if counts[a] + counts[b] >= N:
      continue
    for c in range(10):
      if counts[a] + counts[b] + counts[c] >= N:
        continue
      for d in range(10):
        if counts[a] + counts[b] + counts[c] + counts[d] >= N:
          continue
        # 계산
        result_num = ((a * 10) + b + (c * 10) + d)
        ten = result_num // 10
        one = result_num % 10
        if ten > 9:
          break

        if counts[a] + counts[b] + counts[c] + counts[d] + counts[ten] + counts[one] == N:
          print(f"{a}{b}+{c}{d}={ten}{one}")
          exit()

print('impossible')