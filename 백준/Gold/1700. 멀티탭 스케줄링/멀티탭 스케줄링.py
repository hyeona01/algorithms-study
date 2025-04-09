import sys

N, K = map(int, sys.stdin.readline().split())
use_list = list(map(int, sys.stdin.readline().rstrip().split()))
# use_list = []
# while len(use_list) < K:
#     use_list += list(map(int, sys.stdin.readline().split()))
multitap = [] # 사용 중인 멀티탭
cnt = 0

for i in range(K):
  if len(multitap) < N and use_list[i] not in multitap: # 멀티탭이 비어있다면
    multitap.append(use_list[i])
    continue
  
  if use_list[i] not in multitap: # 멀티탭에 없다면
    cnt += 1
    late_use = 0
    remove_idx = 0
    for j in range(len(multitap)):
      if multitap[j] not in use_list[i:K]: # 다음에 쓰이지 않는다면 삭제
        remove_idx = j
        break
      if late_use < use_list[i:K].index(multitap[j]):
        late_use = use_list[i:K].index(multitap[j]) # 가장 나중에 사용하는 전자용품 플러그 뽑기
        remove_idx = j
    multitap[remove_idx] = use_list[i] # 새 전자용품 꽂음

print(cnt)