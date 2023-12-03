from collections import deque 
def solution(n, computers):
    visited = [False] * n
    def bfs(x):
        queue = deque([x])    
        while queue:
            q = queue.popleft() 
            visited[q] = True 
            for i, c in enumerate(computers[q]):
                if (not visited[i]) and (c==1): 
                    queue.append(i)
    answer = 0 
    for i in range(n):
        if not visited[i]:
            answer += 1 
            bfs(i)   
    return answer