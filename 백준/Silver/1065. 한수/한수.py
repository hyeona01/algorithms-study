import sys

# 1 ~ 99는 한수
# 100 이상일 떄 검증

N = int(sys.stdin.readline())
total = 0

if N < 100:
  total = N
else:
  for i in range(100, N + 1): # 100부터 N까지 한수인지 판별
    hundrend = i // 100 # 100의 자리
    ten = (i % 100) // 10 # 10의 자리
    one = (i % 100) % 10 # 1의 자리
    if (hundrend - ten) == (ten - one):
      total += 1
  total += 99

print(total)