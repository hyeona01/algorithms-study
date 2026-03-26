def solution(phone_book):
    # 전화번호부 정렬
    phone_book.sort()
    
    # 전화번호부의 전화번호를 모두 순회
    # 인접한 번호의 접두어가 같은 지 확인
    # 일치하면 바로 False 리턴
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            return False
    return True   
    
    # return answer