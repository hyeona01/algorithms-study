import sys

N, M = map(int, sys.stdin.readline().strip().split())
tree_list = list(map(int, sys.stdin.readline().strip().split()))

# 높이 H를 지정하면 H 초과의 나무를 얻을 수 있다.
# M 만큼의 나무를 얻고자할 때 절단기 최댓값

# n 높이의 절단기로 list의 나무를 잘랐을 때 얻게는 나무 높이
def cut_tree(list, n):
  cnt = 0
  for tree in list:
    if tree > n:
      cnt += (tree-n)
  return cnt

pl = 0
pr = max(tree_list)

# 절단기의 높이를 가장 높은 나무의 높이와 0의 중간값으로 비교를 시작함
while True:
  pc = (pl+pr) // 2

  gain_tree = cut_tree(tree_list, pc)
  if gain_tree < M: # 획득한 나무가 적은 경우
    pr = pc-1
  elif gain_tree > M: # 획득한 나무가 충분한 경우
    pl = pc+1
  else: 
    print(pc) # 획득한 나무와 원하는 나무 길이가 같음
    break
  
  # 두 수 중, M과의 차가 양의 작은 수인 것
  if pr < pl:
    if gain_tree > M:
      print(pc)
    else:
      print(pc - 1)
    break