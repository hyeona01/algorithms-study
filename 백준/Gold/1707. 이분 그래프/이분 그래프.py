import sys
from collections import deque

K = int(sys.stdin.readline())

def bipartitie_gragh(adj_list):
  # BSF 큐
  queue = deque([1]) # 1로 시작
  visited = set()
  flag = [None] * (len(adj_list)+1) # 0 또는 1로 분할 확인
  flag[1] = 0 # 루트 노드는 0으로 초기화

  while queue or len(visited) < len(adj_list):
    if not queue: # 인접하지 않은 트리일 경우
      for key in adj_list.keys():
        if key not in visited:
          queue.append(key)
          break

    v = queue.popleft()
    f = flag[v]
    visited.add(v)

    for item in adj_list[v]:
      if item != v and flag[item] and flag[item] == f: # 자식 노드와 부모 노드의 색이 같으면 False
        return False

      if item not in visited:
        if f == 1:
          flag[item] = 0 
        else:
          flag[item] = 1
        queue.append(item)
    
  return True

for _ in range(K):
  V, E = map(int, sys.stdin.readline().split())
  adj_list = {i: [] for i in range(1, V+1)}
  # 인접 리스트 추가
  for i in range(E):
    u, v = map(int, sys.stdin.readline().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
  if bipartitie_gragh(adj_list): print('YES') 
  else: print('NO')
