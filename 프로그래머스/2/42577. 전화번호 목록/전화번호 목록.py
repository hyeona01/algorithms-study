def solution(phone_book):
    # 해시 자료구조로 저장
    hash_dict = {}
    for phoneNum in phone_book:
        # hash_dict[hash(phoneNum)] = phoneNum
        hash_dict[phoneNum] = 1
    
    for number in phone_book:
        temp = ""
        for i in range(len(number) - 1):
            temp += number[i]
            if temp in hash_dict: 
                return False
    return True
    
    
    # return answer