# 1966번 프린터 큐

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
  n, m = map(int, sys.stdin.readline().split())
  lst = list(map(int, sys.stdin.readline().split()))
  docs = deque()
  for i in range(len(lst)):
    docs.append((i, lst[i]))

  cnt = 0 # 몇 번째에 출력되는지
  while docs:
    prior_doc = max(docs, key=lambda x: x[1])

    doc = docs.popleft()
    if prior_doc[1] == doc[1]: # 우선순위가 가장 높은 문서라면 인쇄
      cnt += 1
      if doc[0] == m:
        print(cnt)
        break
    else: # 아니면 다시 큐에 추가
      docs.append(doc)
