from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 피로도: k, dungeons: [필요, 소모]
    
    # 던전은 1~8개
    # 모든 경우를 고려해야 함
    # 1. 던전 순서는 permutations를 활용하여 모든 조합 구비
    temp = []
    for i in range(len(dungeons)):
        temp.append(i)
    order = list(permutations(temp, len(dungeons)))
    
    max_play = 0
    # 2. 순서에 따라 k를 소모 피로도 만큼 감소 시키며, 필요 피로도에 충족하는 지 확인
    for o in order:
        curr = k
        cnt = 0
        for idx in o:
            # 필요 피로도가 충분할 때 탐험
            if curr >= dungeons[idx][0]:
                cnt += 1
                curr -= dungeons[idx][1]
            # 3. 피로도가 충분치 않다면 종료
            else:
                break
        # 4. maximum 값 업데이트
        max_play = max(cnt, max_play)
    
    return max_play