def solution(numbers, target):
    cnt = 0
    
    # DFS 구현체
    def dfs(idx, sum_nums):
        nonlocal cnt
        
        # 종료 조건: numbers 길이만큼 연산했을 때 return
        if idx == len(numbers):
            if sum_nums == target:
                cnt += 1
            return cnt

        # 수행 방법: 더하기, 빼기의 경우를 재귀적으로 연산
        dfs(idx + 1, sum_nums + numbers[idx])
        dfs(idx + 1, sum_nums - numbers[idx])
    
    dfs(0, 0)
    
    return cnt