import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
area = []

max_height = 0 # 입력 지역 중 가장 높은 지역의 높이

for i in range(N):
  lst = list(map(int, sys.stdin.readline().split()))
  area.append(lst)
  max_height = max(max(lst), max_height)

dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [-1, 1, 0, 0] # 상 하 좌 우

# 잠기는 높이 / 행 / 열 / 방문한 원소의 배열(T or F)
def check_border(height, r, c, visited):
  # 상하좌우 DFS
  for i in range(4):
    nr = r + dx[i] # 다음 행
    nc = c + dy[i] # 다음 열
    
    if 0 <= nr < N and 0 <= nc < N: # 다음 원소가 유효한 범위 내에 있는지 확인
        if not visited[nr][nc] and area[nr][nc] > height:
            visited[nr][nc] = True
            check_border(height, nr, nc, visited) # 재귀적으로 DFS 탐색

# 메인 함수 - 0부터 가장 높은 높이까지 안전 영역 연산
def safty_area():
    global max_height
    max_safty_area = 0

    for height in range(max_height + 1):  # 높이 0부터 max_height까지
        visited = [[False] * N for _ in range(N)] # 초기화
        count = 0 # 초기화

        for i in range(N): # 행
            for j in range(N): # 열
                if not visited[i][j] and area[i][j] > height: # 방문하지 않거나 안전 영역일 경우
                    check_border(height, i, j, visited)
                    count += 1
        max_safty_area = max(max_safty_area, count)
    return max_safty_area

print(safty_area())