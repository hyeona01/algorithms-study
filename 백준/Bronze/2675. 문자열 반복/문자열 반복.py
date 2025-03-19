import sys

N = int(sys.stdin.readline())

for _ in range(N):
  n, string = map(str, sys.stdin.readline().split())
  result = ''

  for charactor in string:
    result += charactor * int(n)
  
  print(result)