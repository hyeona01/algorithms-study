import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  applicants = []

  for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    applicants.append((a, b))
  
  applicants.sort() # a 기준 오름차순 정렬
  max_cnt = N
  min_rank = applicants[0][1]
  for i in range(1, N):
    if applicants[i][1] > min_rank: # a 성적도 낮으면서 b 성적도 낮을 경우
      max_cnt -= 1
    else:
      min_rank = applicants[i][1] # b 성적이 높은 경우 min_rank 업데이트
  
  print(max_cnt)