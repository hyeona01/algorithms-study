import sys
from collections import deque

class Node:
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent

N = int(sys.stdin.readline())
root = Node(1)
tree = {1: root} # key: value / value: Node객체
adj_list = {i: [] for i in range(1, N+1)}

# 인접 리스트 정의
for i in range(N-1):
  a, b = map(int, sys.stdin.readline().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

queue = deque([1])

while queue:
  v = queue.popleft()
  lst = adj_list[v] # 부모 노드의 인접 노드 리스트
  for n in lst:
    if n not in tree: # 상위 노드는 제외
      tree[n] = Node(n, tree[v])
      queue.append(n) # 하위 노드는 스택에 추가

for i in range(2, N  + 1):
  print(tree[i].parent.value)