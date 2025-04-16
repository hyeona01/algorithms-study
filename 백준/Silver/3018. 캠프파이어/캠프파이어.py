import sys


N = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())
info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(E)]
participants = [True] * (N+1)

for i in range(E):
  p = set(info[i][1:]) # 인원수 정보 제거
  # 선영이가 참여함
  if 1 in p:
    for j in range(1, N + 1): # 없는 인원 찾기
        if participants[j] and j not in p:
          participants[j] = False # 참여하지 않아 노래를 모름
  else:
    # 선영이가 참여하지 않음
    # 직전까지 모든 노래를 아는 사람이 포함되었다면 모든 사람에게 공유됨
    know = False 
    for j in p:
      if participants[j] == True:
          know = True
          break
    for pa in p:
      participants[pa] = True

participants[1] = True
for p in range(1, N+1):
  if participants[p]:
    print(p, end=' ')