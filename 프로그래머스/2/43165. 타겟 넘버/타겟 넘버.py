cnt = 0

def dfs(t, numbers, idx, sum_nums):
    global cnt
    
    # 종료 조건: numbers 길이만큼 연산했을 때 return
    # print("idx",idx)
    # print("sum_nums, target",sum_nums, t)
    # print("cnt",cnt)
    if idx == len(numbers):
        if sum_nums == t:
            cnt += 1
        return cnt

    # 수행 방법: 더하기, 빼기의 경우를 재귀적으로 연산
    dfs(t, numbers, idx + 1, sum_nums + numbers[idx])
    dfs(t, numbers, idx + 1, sum_nums - numbers[idx])
    
def solution(numbers, target):
    global cnt
    
    dfs(target, numbers, 0, 0)
    
    return cnt