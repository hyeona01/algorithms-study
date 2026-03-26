from itertools import permutations

# 소수 판별 함수
def prime(num):
    if num < 2: 
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: 
            return False

    return True

def solution(numbers):
    answer = 0
    numbers_arr = list(numbers)
    
    # 중복 없는 조합
    combi = set()
    
    # 길이 1부터 numbers 최대 길이만큼의 순서 있는 모든 조합 만들기
    for l in range(1, len(numbers_arr) + 1):
        for item in permutations(numbers_arr, l):
            combi.add(int("".join(item)))
    print(combi)
    
    # 모든 조합 중 소수 count
    for num in combi:
        if prime(num): answer += 1
    
    return answer