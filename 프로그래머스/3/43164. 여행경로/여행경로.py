def solution(tickets):
    answer = []
    tickets.sort()
    visited = [False] * len(tickets)
    
    answer.append('ICN')
    
    def dfs(start):
        # 종료 조건: 전부 방문
        if len(answer) == len(tickets) + 1:
            return
        
        # 진행 방법
        for i in range(len(tickets)):
            arr = tickets[i][0]
            dest = tickets[i][1]
            
            if start == arr and not visited[i]:
                visited[i] = True
                answer.append(dest)
                dfs(dest)
                if len(answer) == len(tickets) + 1:
                    return
                
                # 실패 시 백트래킹
                answer.pop()
                visited[i] = False
    
    dfs('ICN')
    
    return answer