import sys
from itertools import combinations

N, C = map(int, sys.stdin.readline().strip().split())
home_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
home_list.sort()

result = 0
start = 1 # 가장 짧은 공유기 거리
end = home_list[-1] - home_list[0] # 가장 긴 공유기 거리

while start <= end:
  margin = (start + end) // 2

  current = home_list[0]
  count = 1

  for i in range(1, N): # 1번집 ~ 마지막집
    if home_list[i] >= current + margin:
      count += 1
      current = home_list[i]

  # 설치한 수가 목표한 수 보다 많을 경우, 거리를 넓혀야 함
  if count >= C: # C 개를 설치할 수 있는 여러 경우의 수 중, 거리를 최대로.
    result = margin # 일단 저장해두고, 더 멀리 설치할 수 있는지 확인
    start = margin + 1

  # 설치한 수가 목표한 수 보다 적을 경우, 거리를 좁혀야 함
  elif count < C:
    end = margin - 1

print(result)