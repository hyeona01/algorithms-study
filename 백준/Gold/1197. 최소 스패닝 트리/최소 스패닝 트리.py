import sys
sys.setrecursionlimit(10**6)

V, E = map(int, sys.stdin.readline().split())
edges = []
parents = [i for i in range(V + 1)]

for i in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  edges.append((a, b, c))

edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 오름차순 정렬

mst_cost = 0

def find(x):
  if parents[x] == x:
    return x
  parents[x] = find(parents[x])
  return parents[x] # 부모 노드를 따라 재귀적으로 루트 노드 찾기

def union(a , b):
  rootA = find(a)
  rootB = find(b)

  if rootA == rootB: # 사이클 발견
    return False
  
  if rootA < rootB:
    parents[rootB] = rootA
  else:
    parents[rootA] = rootB
  return  True # 사이클 없음

for a, b, c in edges:
  if union(a, b): # 사이클 없을 때
    mst_cost += c

print(mst_cost)