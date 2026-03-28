from collections import deque
import heapq

def solution(priorities, location):
    # location 인덱스의 프로세스가 실행되는 순서 return
    # 1. 대기 큐 첫 순서를 꺼낸다.
    # 2-1. 나머지 원소 중 우선순위가 높은 A 원소가 있다면 그 이전 원소는 모두 맨 뒤로 보내며, A 원소를 먼저 처리한다.
    # 2-2. 나머지 원소 중 우선순위가 높은 원소가 없다면 그대로 처리한다.
    
    # 기존 location의 인덱스를 기억하기 위해 새로운 배열 생성
    processes = deque()
    for i in range(len(priorities)):
        processes.append([i, priorities[i]]) # [인덱스, 우선순위][]
    
    cnt = 0
    max_priority = max(priorities)
    while len(processes) > 0:
        curr = processes.popleft()
        
        # 우선순위 높은 프로세스가 존재할 경우
        if curr[1] < max_priority:
            processes.append(curr)
            continue

        # 우선순위 높은 프로세스가 존재하지 않을 경우
        cnt += 1
        
        # location 프로세스일 경우 return
        if curr[0] == location:
            return cnt
        
        priorities.remove(max_priority)
        max_priority = max(priorities)
