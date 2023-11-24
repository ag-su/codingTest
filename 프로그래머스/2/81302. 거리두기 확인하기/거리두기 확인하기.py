from collections import deque 
def bfs(x, y, place, memo, visited): 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)]) 
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4): 
            score = 0
            nx, ny = x+dx[i], y+dy[i]
            
            if nx<0 or nx>4 or ny<0 or ny>4:
                continue 
            
            if place[nx][ny] == "X":
                continue
                
            if not visited[nx][ny]:
                visited[nx][ny] = True
                
                if (place[nx][ny] == "P") and (memo[x][y] <= 1): 
                    return False 
                
                if memo[x][y] >= 1: 
                    continue 
                
                memo[nx][ny] = memo[x][y] + 1 
                queue.append((nx, ny))

    return True
            
                                
def solution(places):
    answer = []

    for place in places:
        flag = True 
        for i in range(5):
            for j in range(5):
                visited = [[False]*5 for _ in range(5)]
                memo = [[0]*5 for _ in range(5)]
                if place[i][j] == 'P' and not bfs(i, j, place, memo, visited):
                    flag = False 
                    break
            if not flag:
                break
                
        answer.append(int(flag))
    
    return answer