def solution(triangle):
    
    # idx, idx+1 이동 가능
    # dp[depth][idx] = max(dp[depth-1][idx] + i, dp[depth-1][idx-1] + i)
    
    dp = []
    for i in range(1, len(triangle) + 1):
        dp.append([0] * i)
    
    # dp 초기화
    dp[0][0] = triangle[0][0]
    for depth in range(1, len(triangle)):
        for idx in range(depth+1):
            if idx == 0:
                dp[depth][idx] = dp[depth-1][idx] + triangle[depth][idx]
            elif idx == depth:
                dp[depth][idx] = dp[depth-1][idx-1] + triangle[depth][idx]
            else:
                dp[depth][idx] = max(dp[depth-1][idx] + triangle[depth][idx], dp[depth-1][idx-1] + triangle[depth][idx])
                
                
    return max(dp[-1])