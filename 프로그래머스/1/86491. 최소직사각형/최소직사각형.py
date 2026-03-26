def solution(sizes):
    answer = 0
    
    width = 0
    height = 0
    
    # 가로, 세로 길이 중 긴 길이를 width에 저장한다.
    # 그외 길이를 height에 저장한다.
    for a, b in sizes:
        if a > b:
            w, h = a, b
        else:
            w, h = b, a
        
        # 최대 길이를 업데이트 한다.
        if w > width: width = w
        if h > height: height = h
        
    answer = width * height 
    
    return answer