import sys

n, k = map(int, sys.stdin.readline().split())

gold_list = [0] * (n+1)
silver_list = [0] * (n+1)
bronze_list = [0] * (n+1)

# 입력 받기
for _ in range(n):
  num, gold, silver, bronze = map(int, sys.stdin.readline().split())
  gold_list[num] = gold
  silver_list[num] = silver
  bronze_list[num] = bronze

result = 1
# 순위 결정
for i in range(1, n+1):
  if i == k:
    continue

  if gold_list[i] > gold_list[k]:
    result += 1
    continue
  elif gold_list[i] == gold_list[k]:
    if silver_list[i] > silver_list[k]:
      result += 1
      continue
    elif silver_list[i] == silver_list[k]:
      if bronze_list[i] > bronze_list[k]:
        result += 1
        continue

print(result)