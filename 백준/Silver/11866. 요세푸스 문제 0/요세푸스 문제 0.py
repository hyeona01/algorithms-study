import sys

N, K = map(int, sys.stdin.readline().split())
# 라이브러리 사용하지 않고, 링 버퍼로 풀어보자. 

ring_buffer = []
rear = N-1
move = 0

for i in range(1, N+1):
  ring_buffer.append(i)

def dequeue(idx):
  global rear

  # 제거할 인덱스가 0보다 같거나 크고 rear 보다 작으면 단순 삭제
  if 0 <= idx < rear:
    print(ring_buffer[idx], end=', ')
    # 한칸씩 앞으로 이동
    for i in range(idx+1, rear+1):
      ring_buffer[i-1] = ring_buffer[i] # 삭제
    ring_buffer[rear] = 0
    rear -= 1

  # 제거할 인덱스가 rear와 같다면
  elif idx == rear:
    print(ring_buffer[idx], end=', ')
    ring_buffer[idx] = 0
    rear -= 1

print('<', end='')
while rear > 0:
  move += (K-1)
  while move > rear:
    move = move - rear - 1
  dequeue(move)

print(ring_buffer[0], end='>')