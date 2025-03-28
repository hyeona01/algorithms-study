import sys
sys.setrecursionlimit(100000)

def postorder(start, end):
  if start > end: # base case
      return
  
  mid = end + 1 # 오른쪽 서브트리의 루트노드
  for i in range(start+1, end+1):
      if tree[start] < tree[i]: # 오른쪽 노드 발견
          mid = i
          break
  postorder(start+1, mid-1) # 왼쪽 서브트리
  postorder(mid, end) # 오른쪽 서브트리
  print(tree[start]) # 부모 노드

tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline().strip()))
    except:
        break

postorder(0, len(tree) - 1)