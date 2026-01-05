N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input()) # 문자열로 삽입

firstColor = 'W'
minCnt = 64

for row in range(N-8+1):
    for col in range(M-8+1):
        for start in ['W', 'B']:  # 두 시작 색 모두 고려
            cnt = 0
            for i in range(8):
            # 색 결정
                if i % 2 == 0:
                    current = start
                else:
                    if start == 'W':
                        current = 'B'
                    else:
                        current = 'W'
                for j in range(8):
                    if current != board[row+i][col+j]:
                        cnt += 1
                    
                    # 색 바꾸기
                    if current == 'W':
                        current = 'B'
                    else:
                        current = 'W'
            # 8X8 연산 완료
            if minCnt > cnt:
                minCnt = cnt

print(minCnt)