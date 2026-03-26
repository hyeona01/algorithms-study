def solution(participant, completion):
    # 정렬
    participant.sort()
    completion.sort()
    
    # 비교 후 다른 선수를 발견하면 return
    for i in range((len(completion))):
        if participant[i] != completion[i]:
            return participant[i]
    
    # 전부 비교했는데도 없으면 마지막 선수 return
    return participant[-1]
    
    
    # return answer