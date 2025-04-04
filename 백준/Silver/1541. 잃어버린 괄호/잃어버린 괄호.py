import sys

lst = list(sys.stdin.readline().strip().split('-'))
result = 0

plus_nums = list(map(int, lst[0].split('+')))
result += sum(plus_nums)

for minus_idx in range(1, len(lst)):
  plus_nums = list(map(int, lst[minus_idx].split('+')))
  result -= sum(plus_nums)

print(result)