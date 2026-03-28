from collections import deque

def bfs(grid, characterX, characterY, itemX, itemY):
    visited = {(characterX, characterY)}
    # x좌표, y좌표, 이동 횟수
    queue = deque()
    queue.append([characterX, characterY, 0])
    
    # 상하좌우
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while len(queue) > 0:
        x, y, cnt = queue.popleft()
        
        # 목표 좌표 도달
        if x == itemX and y == itemY:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 1. 범위 내, 2. 방문하지 않은 좌표 3. 이동 가능한 좌표
            if 0 <= nx < 102 and 0 <= ny < 102 and (nx, ny) not in visited and grid[ny][nx]:
                queue.append([nx, ny, cnt + 1])
                visited.add((nx, ny))
    return 0

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 모든 직사각형의 공간을 1로 채워넣기
    # 2. 내부를 0으로 
    # 3. 캐릭터 좌표에서 BFS로 목표 위치에 도달
    
    grid = []
    for _ in range(102):
        grid.append([0] * 102)
    
    for rect in rectangle:
        x1, y1, x2, y2 = [v*2 for v in rect]

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[y][x] = 1

    for rect in rectangle:
        x1, y1, x2, y2 = [v*2 for v in rect]
        
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                grid[y][x] = 0
            
    answer = bfs(grid, characterX*2, characterY*2, itemX*2, itemY*2)
    
    return answer / 2