import sys

def avg(score_list): # 리스트 형태로 받음
  return sum(score_list) / len(score_list)


C = int(sys.stdin.readline())

for _ in range(C):
  input = list(map(int, sys.stdin.readline().split()))
  N = input[0]
  scores = input[1:]
  
  # 평균 구하기
  score_avg = avg(scores)

  # 평균 점수 이상의 학생 수 구하기
  cnt = 0
  for score in scores:
    if score_avg < score:
      cnt += 1

  # 평균 이상 학생 수 / 전체 학생 수
  print(f'{(cnt / N * 100):.3f}%')