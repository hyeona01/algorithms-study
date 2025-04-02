import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
edges = []

for i in range(1, M+1):
	x, y = map(int, sys.stdin.readline().split())
	edges.append((x, y, i)) # x, y, cost
edges.sort(key = lambda x: x[2])

def find(v):
	if v == parents[v]:
		return v
	parents[v] = find(parents[v])
	return parents[v]

def union(v, u):
	pv = find(v)
	pu = find(u)

	if pv == pu:
		return False # 사이클 존재
	else:
		if pv < pu:
			parents[pu] = pv
		else:
			parents[pv] = pu
		return True # 사이클 없음 - 연산 완료

for game in range(K):
	mst = 0
	parents = [i for i in range(0, N+1)] # 1번 인덱스부터 시작
	current_edges_idx = []
	mst_edges_cnt = 0 # 신장 트리는 노드가 V개일 때 간선이 V-1개여야 함

	for i in range(len(edges)):
		if union(edges[i][0], edges[i][1]): # x, y union 연산
			mst += edges[i][2] # 가중치 더하기
			mst_edges_cnt += 1
			current_edges_idx.append(i)

	if mst_edges_cnt == N-1:
		print(mst, end=' ')
	else:
		print(0, end=' ')
	
	edges.pop(current_edges_idx[0]) # 이번 턴에서 구한 MST에서 가장 가중치가 작은 간선