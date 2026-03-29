import math
H, W, N, M = map(int, input().split())

# 1. 구현
# (0, 0) 착석, N개의 행을 비우고 착석 가능, M개의 열을 비우고 착석 가능
# cnt = 0
# for i in range(0, H, N + 1):
#     for j in range(0, W, M + 1):
#         cnt += 1
# print(cnt)

# 2. 시간초과 개선
# 5 4 1 1
# 착석 가능한 행의 수: H / N+1의 올림
# 착석 가능한 열의 수: W / M+1의 올림
print(math.ceil(H/(N+1)) * math.ceil(W/(M+1)) )