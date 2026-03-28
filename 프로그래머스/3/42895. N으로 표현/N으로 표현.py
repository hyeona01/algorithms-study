def solution(N, number):
    answer = 0
    # +, -, *, //
    
    # 1 2 3 4 5 6 7 8
    # N i개로 할 수 있는 사칙 연산으로 모두 채워넣고,
    # NN, NNN으로 확장!
    # dp[i] = ((dp[i-1] OP dp[1]), (dp[i-2] OP dp[2]), ...)
    
    dp = [set() for _ in range(9)] # 8 초과 시 -1 return
    for _ in range(9):
        dp.append(set())
    
    for i in range(1, 9):
        dp[i] = set()
        dp[i].add(int(str(N)*i)) # NNNN
        for j in range(1, i):
            for num_a in dp[j]:
                for num_b in dp[i-j]:
                    dp[i].add(num_a + num_b)
                    dp[i].add(num_a - num_b)
                    dp[i].add(num_a * num_b)
                    if num_a != 0 and num_b != 0:
                        dp[i].add(num_a // num_b)
        if number in dp[i]:
            return i
    
    return -1