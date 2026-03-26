def solution(word):
    answer = 0
    # 5글자 A E I O U
    # 각 자릿수 별 이동 시의 횟수
    
    # 5번째 자리: 1
    print(1)
    # 4번째 자리: 6
    print(1+5)
    # 3번째 자리:
    print(1+5+25)
    # 2번째 자리:
    print(1+5+25+125)
    # 1번째 자리:
    print(1+5+25+125+625)
    
    fee = [781, 156, 31, 6, 1]
    v = "AEIOU"
    
    answer = 0
    for i in range(len(word)):
        answer += fee[i] * v.index(word[i])
        answer += 1
        
    return answer