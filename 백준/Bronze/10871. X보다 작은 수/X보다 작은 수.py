import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for a in A:
  if(X > a):
    print(a, end= " ")