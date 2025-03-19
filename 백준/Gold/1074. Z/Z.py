# 복습

import sys

n, r, c = map(int, sys.stdin.readline().split())
result = 0

# 백트래킹+재귀로 풀이

def z(n, row, col, order):
  global result
  if n == 1:
    if r == row and c == col:
      result = order
      return
    elif r == row and c > col:
      result = order + 1
      return
    elif r > row and c == col:
      result = order + 2
      return
    else:
      result = order + 3
      return
  
  # n = 3 일 때를 가정함. 
  # 간격: 2^(n-1)
  # 하나의 사분면 사이즈: 2^(n-1) * 2^(n-1)
  # 0 <= row <= 3 and 0 <= col <= 3 -> 0~15
  # 0 <= row <= 3 and 4 <= col <= 7 -> 16~31
  # 4 <= row <= 7 and 0 <= col <= 3 -> 32~47
  # 4 <= row <= 7 and 4 <= col <= 7 -> 48~63

  size = 2 ** (n-1) * 2**(n-1)
  one_side = 2**(n-1)

  if row <= r < row+one_side and col <= c < col + one_side:
    z(n-1, row, col, order + 0) # 1사분면

  elif row <= r < row + one_side and col + one_side <= c < col + 2*one_side:
    z(n-1, row, col + one_side, order + size) # 2사분면

  elif row+one_side <= r < row + 2*one_side and col <= c < col + one_side:
    z(n-1, row + one_side, col, order + size * 2) # 3사분면

  elif row+one_side <= r < row + 2*one_side and col + one_side <= c < col + 2*one_side:
    z(n-1, row + one_side, col + one_side, order + size * 3) # 4사분면

z(n, 0, 0, 0)
print(result)
