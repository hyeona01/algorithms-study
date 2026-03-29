import math

def solution(n, stations, w):
    answer = 0
    
    # 현재 설치된 station +- w 를 제외한 station들의 범위를 각각 탐색
    # 1. stations 기준으로 1번 ~ N번 중 커버되지 않는 범위 탐색
    # 2. 범위 개수 / (2w + 1) -> 올림
    
    last_idx = 1 # 시작 인덱스
    for station in stations:
        min_idx = station - w
        max_idx = station + w
        if last_idx < min_idx:
            not_covered = min_idx - last_idx # 커버되지 않는 좌측 영역 개수
            print(not_covered)
            answer += math.ceil(not_covered / (2 * w + 1))
        last_idx = max_idx + 1
    
    # 마지막 station의 커버되지 않는 우측 영역 처리
    if last_idx <= n:
        not_covered = n - last_idx + 1 # 커버되지 않는 영역 개수
        print(not_covered)
        answer += math.ceil(not_covered / (2 * w + 1))
    return answer