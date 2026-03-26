# from conbination imort itertools

def solution(clothes):
    answer = 0
    
    hash_dict = {}
    # 의상 종류명의 해시 생성
    for item in clothes:
        if item[1] in hash_dict:
            hash_dict[item[1]] += 1
        else:
            hash_dict[item[1]] = 1
    
    # 의상 종류별 아이템 갯수 구하기
    items = list(hash_dict.items())
    # print(items)
    
    # 각 종류의 의상을 입을 경우의 수를 곱하기
    result = 1
    for key, value in items:
        result *= value + 1 # 해당 종류를 입지 않는 경우 고려
        # print(value)
    
    # 모든 의상을 입지 않는 경우 제거
    answer = result - 1
    
    return answer