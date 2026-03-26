def solution(participant, completion):
    sum_hash = 0
    hash_dict = {}    
    
    # 참여자 해시 생성 및 해시 총합 구하기
    for player in participant:
        hash_key = hash(player)
        hash_dict[hash_key] = player
        sum_hash += hash_key
    
    # 완주자 해시를 총합에서 빼기
    for player in completion:
        sum_hash -= hash(player)
    
    # 남은 총합의 해시 value return
    return hash_dict[sum_hash]
    
    # return answer