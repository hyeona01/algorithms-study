import sys
from collections import deque

N = int(sys.stdin.readline())

def card_game(n):
  queue = deque()
  for i in range(1,n+1):
    queue.append(i)

  while len(queue) > 1: # 카드 하나만 남으면 결과 출력
    queue.popleft() # front 버리기
    queue.append(queue.popleft()) # 다음 front를 rear로 옮기기
  
  return queue[0]

print(card_game(N))