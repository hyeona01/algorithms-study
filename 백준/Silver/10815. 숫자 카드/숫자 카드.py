import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

def binary_search(lst, x):
  left = 0
  right = len(lst) - 1

  while left <= right:
    mid = (left+right) // 2

    if x == lst[mid]: return 1 # 찾음
    
    if x > lst[mid]:
      left = mid + 1
    else:
      right = mid - 1

  return 0 # 못찾음

for target in targets:
  print(binary_search(cards, target), end=' ')