# DP 실습
# 1로 만들기

import sys

X = int(sys.stdin.readline())
D = [-1, 0] # 1로 만들기 위해 X가 1일 때는 횟수가 0이다.(0은 불가)

for i in range(2, X+1):
  min_cnt = D[i-1] + 1 # 1 뺀 수 + 1로 초기화
  if i // 3 > 0 and i % 3 == 0: # 3으로 나누어 떨어진다면
    min_cnt = min(min_cnt, D[i//3] + 1)
  if i // 2 > 0 and i % 2 == 0: # 2로 나누어 떨어진다면
    min_cnt = min(min_cnt, D[i//2] + 1)
  D.append(min_cnt)

print(D[-1])