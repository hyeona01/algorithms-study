def solution(brown, yellow):
    answer = []
    
    # yellow 기준, 모든 직사각형 조합 연산
    for x in range(1, yellow + 1):
        # x는 yellow의 약수여야 함
        if yellow % x != 0:
            continue
        
        # yellow 직사각형을 감싸기 위해 필요한 갈색 카펫 갯수
        need = ((x + 2) * 2) + ((yellow // x) * 2)
        
        if need == brown:
            return [yellow // x + 2, x + 2] # 가로 길이가 길도록
    
    # return answer