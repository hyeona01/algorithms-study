import sys

N = int(sys.stdin.readline())

col_list = []
diag_list = [] # 좌측 상향 대각선
diag2_list = [] # 우측 상향 대각선
count = 0

def put_queen(r, c):
  if c in col_list:
    return False
  elif r-c in diag_list:
    return False
  elif r+c in diag2_list:
    return False
  else:
    col_list.append(c)
    diag_list.append(r-c)
    diag2_list.append(r+c)
    return True

# 시작 행은 0, N-1 행의 퀸까지 찾으면 종료
def chess(row):
  global count
  # 종료 조건: 적합한 방법을 찾은 경우
  if row == N:
    count += 1
    return
  
  # -- 적합한지 검증 --
  for col in range(N):
    # 적합할 경우
    if put_queen(row, col):
      chess(row + 1) # 다음 행으로 가기

      # 전체 열을 탐색하였으나, 실패했을 경우 직전 행의 퀸 제거
      col_list.pop(-1)
      diag_list.pop(-1)      
      diag2_list.pop(-1)      
  
chess(0)
print(count)
