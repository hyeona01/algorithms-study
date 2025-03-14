import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

# ---- 시간 초과 ----
# # 날짜 초기화
# days = 1

# # 첫날 낮에 오른 이후 거리
# V -= A

# while V > 0:
#   # 밤에 미끄러진 이후 거리
#   V += B

#   # 오르는 데 소요되는 날짜
#   days += 1

#   # 낮에 오른 이후 거리
#   V -= A
# ---- ---- ----

def resolve(A, B, V):
  # 하루에 다 오르는 경우
  if A >= V:
    return 1

  # 첫날 계산
  V -= A

  # 낮에 다 올랐을 경우
  if V % (A - B) == 0:
    return (V // (A - B)) + 1

  # 나누어 떨어지지 않는다면 다음 날 낮 중간에 끝났다는 의미이기에 하루 추가해야 함(소수점 올림 처리)
  else :
    return int(math.ceil(V / (A - B))) + 1

print(resolve(A, B, V))