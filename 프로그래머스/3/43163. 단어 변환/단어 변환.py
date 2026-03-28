from collections import deque

# 두 단어간 알파벳 차이가 하나인지 검증하는 함수
def is_one_diff(word_a, word_b):
    cnt = 0
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            cnt += 1
            if cnt > 1: return False
    return True

def bfs(begin, target, words):    
    # 최소 거리: BFS
    # 반환 조건
    # 1. taget의 단어에 도달하면 cnt를 반환하며 종료 -> 변환 성공
    # 2. queue가 빈 상태가 되면 0 반환하며 종료 -> 변환 실패
    
    visited = set()
    # 인덱스, 누적 변경 횟수
    queue = deque()
    curr = begin
    
    # queue 초기화
    for i in range(len(words)):
        if is_one_diff(curr, words[i]):
            queue.append((i, 1))
            visited.add(i)
    
    while len(queue) > 0:        
        idx, cnt = queue.popleft()
        curr = words[idx]
        
        # target과 일치하는지 확인
        if curr == target:
            return cnt
        
        for i in range(len(words)):
            # 1. 방문하지 않은 단어, 2. 변환 가능한 단어
            if i not in visited and is_one_diff(curr, words[i]):
                queue.append((i, cnt + 1))
                visited.add(i)
        
    # 변환할 수 없는 경우
    return 0
    

def solution(begin, target, words):    
    if target not in words:
        answer = 0
    
    answer = bfs(begin, target, words)
    
    return answer