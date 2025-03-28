import sys
sys.setrecursionlimit(10**6)

# 경로 압축과 합병시 트리 높이를 기준으로 합치기
def find(parents, rank, x):
  if parents[x] != x:
    parents[x] = find(parents, rank, parents[x])  # 경로 압축
  return parents[x]


def union(parents, rank, a, b):
  rootA = find(parents, rank, a)
  rootB = find(parents, rank, b)

  if rootA == rootB:  # 사이클 발견
    return False

  # 트리 높이를 기준으로 합침
  if rank[rootA] > rank[rootB]:
    parents[rootB] = rootA
  elif rank[rootA] < rank[rootB]:
    parents[rootA] = rootB
  else:
    parents[rootB] = rootA
    rank[rootA] += 1  # 두 트리의 높이가 같으면 한쪽의 높이를 증가시킴
  return True


V, E = map(int, sys.stdin.readline().split())
edges = []
parents = [i for i in range(V + 1)]
rank = [0] * (V + 1)  # 트리의 높이를 저장하는 배열

for i in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  edges.append((a, b, c))

edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 오름차순 정렬

mst_cost = 0
mst_cnt = 0

for a, b, c in edges:
  if union(parents, rank, a, b): # 사이클 없을 때
    mst_cost += c
    mst_cnt += 1
    if V - 1 == mst_cnt: # MST 완성(간선은 V-1개)
      break

print(mst_cost)