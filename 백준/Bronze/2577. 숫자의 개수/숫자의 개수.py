import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

# A,B,C 를 곱하기
result = A * B * C

# 문자열로 변환
result = str(result)

# 0-9까지 몇 번씩 쓰였는지 구하기
for i in range(0, 10):
  print(result.count(str(i)))