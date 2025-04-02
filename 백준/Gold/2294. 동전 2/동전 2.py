import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

coin = []
for _ in range(n):
	temp = int(sys.stdin.readline())
	if temp not in coin:
		coin.append(temp)

# 메모리 초과 방지를 위해 기존에 탐색한 금액은 큐에 추가하지 않음(어차피 기존 결과 보다 크거나 같기 때문)
visited = set()
queue = deque()
def bfs(target):
	queue.append((target, 0)) # (현재 값, 연산 횟수)

	while queue:
		cur_val, level = queue.popleft()
		
		for c in coin:
			next_val = cur_val - c
			if next_val == 0: # 해답을 찾음
				return level + 1
			elif next_val > 0 and next_val not in visited: # 아직 탐색하지 않은 금액이면서 0보다 클 때
				visited.add(next_val)
				queue.append((next_val, level + 1))
	return -1 # 주어진 동전으로 해답을 찾지 못함
print(bfs(k))