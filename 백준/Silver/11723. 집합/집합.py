import sys
from collections import deque

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

m = int(sys.stdin.readline())
S = set()

def calculate(cmd):
  if " " in cmd:
    action, x = cmd.split()
    x = int(x)
  else:
    action = cmd

  if action == 'add':
    S.add(x)
  elif action == 'remove':
    S.discard(x)
  elif action == 'check':
    if x in S:
      print(1)
    else:
      print(0)
  elif action == 'toggle':
    if x in S:
      S.remove(x)
    else:
      S.add(x)
  elif action == 'all':
    for i in range(1, 21):
      S.add(i)
  elif action == 'empty':
    S.clear()
  else:
    print("잘못 입력하셨습니다.")

for _ in range(m):
  calculate(sys.stdin.readline().strip())
