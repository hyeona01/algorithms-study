from collections import deque 

def solution(maps):

    # 캐릭터 (1,1) 상대방(n,m)
    # cnt를 포함하여 bfs 탐색
    
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = set((0, 0))
    # n, m, 거리
    queue = deque([(0, 0, 1)])
    answer = -1
    
    while len(queue) > 0:
        curr = queue.popleft()
        
        # 상대방 진영에 도달하면 중단
        if curr[0] == (n - 1) and curr[1] == (m - 1):
            answer = curr[2] # 거리
            break
        
        # 인접한 노드 큐에 추가
        for d in range(4):
            nx = curr[0] + dx[d]
            ny = curr[1] + dy[d]
            # 1. 유효한 범위 내, 2. 방문하지 않은 칸, 3. 벽이 없는 칸
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny]:
                queue.append((nx, ny, curr[2] + 1))
                visited.add((nx, ny)) # 큐에 삽입과 동시에 방문 처리
    
    return answer