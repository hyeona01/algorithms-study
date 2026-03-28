import math
from collections import deque

def solution(progresses, speeds):
    # 며칠 후 작업이 완료되는 지 계산한 queue 생성
    # pop하며 현재 숫자 이하인 원소는 전부 pop
    
    done = deque()
    for i in range(len(progresses)):
        need_prog = 100 - progresses[i]
        done.append(math.ceil(need_prog / speeds[i]))
    
    deployment = []
    max_date = done.popleft()
    feature = 1
    while len(done) > 0:
        curr = done.popleft()
        # 이전 작업에 포함하여 배포 가능
        if max_date >= curr:
            feature += 1
        # 이후 일정에 배포
        else:
            deployment.append(feature)
            feature = 1
            max_date = curr
    # 마지막 일정 배포
    deployment.append(feature)
    
    return deployment