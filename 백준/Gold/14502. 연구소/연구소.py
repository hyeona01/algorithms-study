import itertools
import copy

N, M = map(int, input().split())
arr = []
empty = []
viros = []
for row in range(N):
    line = list(map(int, input().split()))
    for col in range(M):
        if line[col] == 0:
            empty.append([row, col])
        elif line[col] == 2:
            viros.append([row, col])
    arr.append(line)

# 3개의 조합 찾기
combi = itertools.combinations(empty, 3)

def dfs(arr, x, y):
    # 범위 확인, 0인 것만 갈 수 있음.
    # 상하좌우 움직임
    if not (0 <= x < N and 0 <= y < M) or arr[x][y] != 0:
        return
    arr[x][y] = 2
    dfs(arr, x-1, y)
    dfs(arr, x+1, y)
    dfs(arr, x, y-1)
    dfs(arr, x, y+1)

max_safe = 0
for walls in combi:
    temp_arr = copy.deepcopy(arr)
    for wx, wy in walls:
        temp_arr[wx][wy] = 1
    for vx, vy in viros:
        dfs(temp_arr, vx-1, vy)
        dfs(temp_arr, vx+1, vy)
        dfs(temp_arr, vx, vy-1)
        dfs(temp_arr, vx, vy+1)
    safe = sum(row.count(0) for row in temp_arr)
    if safe > max_safe:
        max_safe = safe

print(max_safe)