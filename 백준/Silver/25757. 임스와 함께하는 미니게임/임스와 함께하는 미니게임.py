N, type = map(str, input().split())

# 종류: Y = 2, F = 3, O = 4
need = 0
if type == 'Y':
    need = 1
elif type == 'F':
    need = 2
elif type == 'O':
    need = 3

play = 0
play_history = set()
waiting = 0
for i in range(int(N)):
    player = input()

    # 이미 플레이한 유저는 패스
    if player in play_history:
        continue

    # 유저 플레이 이력 추가
    play_history.add(player)

    # 대기 인원 추가
    waiting += 1

    # 게임 플레이
    if waiting == need:
        play += 1
        waiting = 0

print(play)