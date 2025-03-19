# 복습

import sys

n = int(sys.stdin.readline())

# 백트래킹 방법 사용: 퀸이 놓여질 자리가 없으면 이전으로 돌아가, 다른 자리로 가봐야 함
# 수직, 수평, 대각선 제외

diag1 = []
diag2 = []
col_list = []
row_list = []
count = 0

def n_queen(row):
  global n
  global count

  if row == n: # 퀸이 n번 전부 놓였을 경우 종료
    count += 1
    return
  
  for col in range(n): # 0 ~ n-1 열에서 각각 시작
    if col not in col_list and (row - col) not in diag1 and (row + col) not in diag2:
      col_list.append(col)
      diag1.append(row - col)
      diag2.append(row + col)
      n_queen(row + 1)
      col_list.pop()
      diag1.pop()
      diag2.pop()

n_queen(0)
print(count)