# 더하기 사이클

import sys

n = int(sys.stdin.readline())

new_nun = n
count = 0

while True:
  ten = new_nun // 10 # 10의 자리
  one = new_nun % 10 # 1의 자리
  a = (ten + one) % 10 # 각 자리를 더한 후 1의 자리

  new_nun = (one * 10) + a
  if new_nun != n:
    count += 1
  else:
    count += 1
    break


print(count)