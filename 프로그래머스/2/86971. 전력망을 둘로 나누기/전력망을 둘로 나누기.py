# dfs로 연결된 노드 수 계산
def dfs(stack, adj_list, visited, cnt):
    if len(stack) == 0: return cnt

    node = stack.pop()
    
    # 이미 방문했다면 스킵
    if node in visited:
        return dfs(stack, adj_list, visited, cnt)
    
    # 방문 처리
    visited.add(node)
    
    # 인접 노드 스택에 추가
    for a in adj_list[node]:
        if a not in visited:
            stack.append(a)
    
    # 재귀 호출
    return dfs(stack, adj_list, visited, cnt + 1)


def solution(n, wires):    
    # 1: 3
    # 2: 3
    # 3: 1, 2, 4
    # 4: 3, 5, 6, 7
    # 5: 4
    # 6: 4
    # 7: 4, 8, 9
    # 8: 7
    # 9: 7
    
    # 1. 인접 리스트를 만든다.
    adj_list = {}
    for i in range(n+1):
        adj_list[i] = []
    for a, b in wires:
        adj_list[a].append(b)
        adj_list[b].append(a)
    print(adj_list)
    
    # 2. 전선을 하나씩 선택해본다.
    min_diff = 100
    for a, b in wires:
        adj_list[a].remove(b)
        adj_list[b].remove(a)
        
        a_cnt = dfs([a], adj_list, set(), 0)
        b_cnt = dfs([b], adj_list, set(), 0)
        
        # 3. 두 전력망의 차이를 계산해서 최소값을 찾는다.
        min_diff = min(min_diff, abs(a_cnt - b_cnt))
        
        # 복구
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    return min_diff