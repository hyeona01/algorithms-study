import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split())))

# 하얀색 0, 파란색 1
white = 0
blue = 0

def recur(n, start_r, start_c, size):
  global white
  global blue
  # base case
  if n <= 0:
    if arr[start_r][start_c] == 0: white += 1
    else: blue += 1    
    return
  
  temp = []
  for i in range(n):
    temp.append(arr[start_r+i][start_c:start_c+n])

  w_cnt = 0
  b_cnt = 0
  for item in temp:
    w_cnt += item.count(0)
  for item in temp:
    b_cnt += item.count(1)

  if w_cnt == size:
    white += 1
  elif b_cnt == size:
    blue += 1

  else:
    next_size = n//2 * n//2
    recur(n//2, start_r, start_c, next_size)
    recur(n//2, start_r, start_c+n//2, next_size)
    recur(n//2, start_r+n//2, start_c, next_size)
    recur(n//2, start_r+n//2, start_c+n//2, next_size)

recur(N, 0, 0, N*N)
print(white)
print(blue)