def solution(n, computers):
    answer = 0
    # 두 컴퓨터 간의 연결 여부 정보 제공
    # 0부터 연결된 노드를 따라서 DFS 순회
    # 한 차례 네트워크 순회가 끝났을 때, 모든 컴퓨터 방문하지 못할 경우, 미방문 컴퓨터부터 다시 DFS 순회
    
    def dfs(visited, stack):
        nonlocal n, computers
        # 종료 조건
        if len(stack) == 0:
            return
        
        # 진행 방법
        node = stack.pop()
        if node in visited:
            dfs(visited, stack)
        
        visited.add(node)
        # node 와 연결된 컴퓨터 전부 stack에 추가
        for idx in range(n):
            if node != idx and computers[node][idx] and idx not in visited:
                stack.append(idx)
        dfs(visited, stack)
    
    visited = set()
    for c in range(n):
        if c not in visited:
            dfs(visited, [c])
            answer += 1
    
    return answer