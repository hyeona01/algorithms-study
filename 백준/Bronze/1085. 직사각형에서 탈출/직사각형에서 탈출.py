import sys

x, y, w, h = map(int, sys.stdin.readline().split())

# x와 w의 차, y와 h의 차, x와 0의 차, y와 0의 차 중 작은 수
print(min(abs(x-w), abs(y-h), abs(x-0), abs(y-0)))