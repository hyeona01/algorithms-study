import sys
from itertools import combinations

M, N, L = map(int, sys.stdin.readline().split())
hunters = list(map(int, sys.stdin.readline().split()))
animals = []
catch = [False] * N

for i in range(N):
  animals.append(list(map(int, sys.stdin.readline().split())))

def catch_animal(x, a_x, a_y): # x좌표의 사대에서 r,c의 동물을 잡을 수 있는지
  # for i in range(x+1):
  if 0<=a_y<=L:
    valid_c = L-a_y
    if x-valid_c <= a_x <= x+valid_c:
      return True
  return False

count = 0
for i in range(N): # 동물들마다 순회
  a_x = animals[i][0]
  a_y = animals[i][1]
  for x in hunters: # 해당 동물이 헌터들에게 잡히는지 순회
    if catch[i] == False and catch_animal(x, a_x, a_y):
      catch[i] = True
      count += 1

print(count)
# print(catch)