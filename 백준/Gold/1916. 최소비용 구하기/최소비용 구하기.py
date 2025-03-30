import sys

def find_min_cost():
    min_cost = float('inf')
    idx = -1
    for i in range(1, N + 1):
        if not visited[i] and cost[i] < min_cost:
            min_cost = cost[i]
            idx = i
    return idx

def dijkstra(start):
    cost[start] = 0

    for _ in range(N):  # 모든 노드를 방문할 때까지
        next = find_min_cost()
        if next == -1:  # 더 이상 방문할 노드가 없으면 종료
            break
        visited[next] = True  # 방문 처리

        for i in range(1, N + 1):  # 모든 노드 확인
            if dp[next][i] != INF and not visited[i]:  # 연결된 노드이고, 방문하지 않았다면
                new_cost = cost[next] + dp[next][i]
                if new_cost < cost[i]:  # 최소 비용 갱신
                    cost[i] = new_cost

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = float('inf')

dp = [[INF] * (N + 1) for _ in range(N + 1)]
cost = [INF] * (N + 1)
visited = [False] * (N + 1)

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    dp[s][e] = min(dp[s][e], c)  # 중복 간선 처리

start, end = map(int, sys.stdin.readline().split())

dijkstra(start)
print(cost[end])