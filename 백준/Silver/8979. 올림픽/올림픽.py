import sys

n, k = map(int, sys.stdin.readline().split())

gold_list = [0] * n
silver_list = [0] * n
bronze_list = [0] * n

# 입력 받기
for i in range(n):
  num, gold, silver, bronze = map(int, sys.stdin.readline().split())
  gold_list[i] = gold
  silver_list[i] = silver
  bronze_list[i] = bronze

result = 1
# 순위 결정
for i in range(n):
  if gold_list[i] > gold_list[k]:
    result += 1
    break
  elif gold_list[i] == gold_list[k]:
    if silver_list[i] > silver_list[k]:
      result += 1
      break
    elif silver_list[i] == silver_list[k]:
      if bronze_list[i] > bronze_list[k]:
        result += 1
        break

print(result)