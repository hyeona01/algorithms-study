class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
  def preorder(self, node):
    if node:
      print(node.value, end='')
      self.preorder(node.left)
      self.preorder(node.right)
      
  def inorder(self, node):
    if node:
      self.inorder(node.left)
      print(node.value, end='')
      self.inorder(node.right)

  def postorder(self, node):
    if node:
      self.postorder(node.left)
      self.postorder(node.right)
      print(node.value, end='')

import sys
N = int(sys.stdin.readline())
tree = {}

for i in range(N):
  root, left, right = map(str, sys.stdin.readline().strip().split())

  if root not in tree:
    tree[root] = Node(root)

  if left != '.':
    if left not in tree:  # 이미 존재하는 노드를 덮어쓰지 않도록!
      tree[left] = Node(left) # 없다면 새로 노드 생성
    tree[root].left = tree[left] # 있다면 부모-자식 노드 연결

  if right != '.':
    if right not in tree:  # 이미 존재하는 노드를 덮어쓰지 않도록!
      tree[right] = Node(right) # 없다면 새로 노드 생성
    tree[root].right = tree[right] # 있다면 부모-자식 노드 연결
# print(tree)

root = tree['A']
root.preorder(root)
print()
root.inorder(root)
print()
root.postorder(root)