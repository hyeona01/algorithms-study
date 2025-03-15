import sys

N, r, c = map(int, sys.stdin.readline().split())

# key: 찾고자 하는 행(r)과 열(c)을 주어진 배열 크기의 4등분을 하며 찾는다.

# (1) 2의 N-1승 * 2의 N-1승 으로 4등분을 한다.
# (2) 어느 사분면에 찾고자 하는 r, c가 속하는 지 찾는다.
# (3) 해당 사분면의 시작점만큼 count를 증가시킨다.
# (4) (2) ~ (4)를 반복하고, 
#      N == 1가 된다면 r, c와 일치하는 분면에 맞게 count를 증가시켜준다.

def recursive_z(n, x, y, count):
  # (4) 종료 조건 설정
  if n == 1:
    if r == x and c == y:
      return count
    elif r == x and c > y:
      return count + 1
    elif r > x and c == y:
      return count + 2
    else:
      return count + 3
  
  # (1) 4등분한다.
  section = 2 ** (n-1)

  # (2, 3) 어느 사분면에 속하는지 판단하고 해당 사분면의 시작점만큼 count를 설정한다.
  if r < x+section and c < y+section: # 제1사분면
    return recursive_z(n-1, x, y, count)
  elif r < x+section and c >= y+section: # 제2사분면
    return recursive_z(n-1, x, y+section, count + section*section)
  elif r >= x+section and c < y+section: # 제3사분면
    return recursive_z(n-1, x+section, y, count + section*section*2)
  elif r >= x+section and c >= y+section: # 제4사분면
    return recursive_z(n-1, x+section, y+section, count + section*section*3)

# x, y의 시작점은 (0,0)으로 세팅하며 count를 초기화한다.
print(recursive_z(N, 0, 0, 0))