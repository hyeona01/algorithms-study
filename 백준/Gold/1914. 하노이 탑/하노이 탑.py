# 복습

import sys

n = int(sys.stdin.readline())

def hanoi(n, start, temp, end):
  # 변수 정의
  # 1. 원판의 출발지, 원판의 도착지, 원판의 경유지
  # 2. 원판의 개수
  if n == 1:
    # print(f'{n}원판이 {start}에서 {end}로 이동')
    print(start, end)
    return
  hanoi(n-1, start, end, temp)
  hanoi(1, start, temp, end)
  hanoi(n-1, temp, start, end)

print(2**n - 1)
if n <= 20:
  hanoi(n, 1, 2, 3)