from collections import Counter

def solution(participant, completion):
    # Counter로 풀이
    part_counter = Counter(participant)
    comp_counter = Counter(completion)
    # print(part_counter)
    
    # 빼기 연산
    answer = part_counter - comp_counter
    answer = list(answer.keys())
    # print(answer)
    
    return answer[0]