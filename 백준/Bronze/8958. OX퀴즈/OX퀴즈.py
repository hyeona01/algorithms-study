import sys

N = int(sys.stdin.readline())
scores_list = [sys.stdin.readline() for _ in range(N)]

for scores in scores_list:
  cnt = 1
  result = 0
  for score in scores:
    if score == 'O':
      result += cnt
      cnt += 1
    elif score == 'X':
      cnt = 1
  print(result)